from flask import Flask, request, render_template, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql.elements import Null
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret" 
debug=DebugToolbarExtension(app)

from models import db, connect_db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True       

connect_db(app)

@app.route('/')
def list_pets():
    """Homepage lists pets and availability status with photo"""

    pets = Pet.query.all()

    return render_template('list_pets.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Form for adding new pet, redirects to pet page on submit"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        breed = form.breed.data
        sex = form.sex.data
        if form.image_url.data != '':
            image_url = form.image_url.data
        else: 
            image_url = 'https://us.123rf.com/450wm/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg?ver=6'
        age_years = form.age_years.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, breed=breed, image_url=image_url, age_years=age_years, sex=sex, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f'Successfully added {name}')
        return redirect(f'/{pet.id}')
        
    else: 
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def view_pet(pet_id):
    """Show the pet with info and availability status"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.breed = form.breed.data
        pet.sex = form.sex.data
        if form.image_url.data != '':
            pet.image_url = form.image_url.data
        else: 
            pet.image_url = 'https://us.123rf.com/450wm/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg?ver=6'
        pet.age_years = form.age_years.data
        pet.notes = form.notes.data

        db.session.add(pet)
        db.session.commit()
        flash(f'Successfully edited {pet.name}')
    return render_template('view_pet.html', pet = pet)

@app.route('/<int:pet_id>/edit')
def edit_pet(pet_id):
    """Show pre-populated form to edit the pet, redirect to pet page on submit"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    form.name.data = pet.name
    form.species.data = pet.species
    form.breed.data = pet.breed
    form.sex.data = pet.sex
    form.image_url.data = pet.image_url
    form.age_years.data = pet.age_years
    form.notes.data = pet.notes
    return render_template('edit_pet_form.html', form=form, pet=pet)