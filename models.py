from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet model"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    species = db.Column(db.String, nullable = False)
    sex = db.Column(db.String, nullable = False)
    breed = db.Column(db.String, nullable = True)
    image_url = db.Column(db.String, server_default='https://us.123rf.com/450wm/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg?ver=6')
    age_years = db.Column(db.Float, nullable = True)
    notes = db.Column(db.String, nullable = True)
    available = db.Column(db.Boolean, default = True)