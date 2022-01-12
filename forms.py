from re import U
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, BooleanField, FileField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, AnyOf, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding new pet"""
    name = StringField('Pet Name')
    species = StringField('Species', validators=[InputRequired(), AnyOf(values=['dog', 'cat', 'rabbit', 'porcupine'])])
    sex = SelectField('Sex', choices=[('f', 'Female'),('m', 'Male')])
    breed = StringField('Breed')
    age_years = FloatField('Age in Years', validators=[NumberRange(min=0, max=30)])
    image_url = StringField('Photo URL', validators=[URL()])
    notes = TextAreaField('Notes')

class EditPetForm(FlaskForm):
    """Form for editing a pet"""
    name = StringField('Pet Name')
    species = StringField('Species', validators=[InputRequired(), AnyOf(values=['dog', 'cat', 'rabbit', 'porcupine'])])
    sex = SelectField('Sex', choices=[('f', 'Female'),('m', 'Male')])
    breed = StringField('Breed')
    age_years = FloatField('Age in Years', validators=[NumberRange(min=0, max=30)])
    image_url = StringField('Photo URL', validators=[URL()])
    notes = TextAreaField('Notes')


