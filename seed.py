"""Seed file to make sample data for pets db.""" 
from models import Pet, db 
from app import app 

# Create all tables 
db.drop_all()
db.create_all() 


# If table isn't empty, empty it
Pet.query.delete()


# Add pets
whiskey = Pet(name = 'Whiskey', species = "dog", sex = 'f', breed = 'beagle', age_years = 11, image_url = 'https://macybaybeagles.weebly.com/uploads/1/9/7/5/19755231/published/img-0177-2_2.jpeg?1563044217')
bowser = Pet(name = 'Bowser', species = "dog", sex = 'm', breed = 'chihuahua', available = False, notes = 'Pending neuter surgery', age_years = 5)
spike = Pet(name = 'Spike', species = "rabbit", sex = 'm', age_years = 3, image_url = 'https://rabbit.org/articles/wp-content/uploads/2021/07/12-24-2019-7-andre.jpg')

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike) 
				
# Commit--otherwise, this never gets saved!
db.session.commit()
