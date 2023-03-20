from app         import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 

class Fundraisers(db.Model):

    __tablename__ = 'Fundraisers'

    id       = db.Column(db.Integer,     primary_key=True)
    name     = db.Column(db.String(64),  unique = True)
    amount    = db.Column(db.Integer)
    summary   = db.Column(db.String(64))
    created_by = db.Column(db.String(64))
    image_file = db.Column(db.String(20), nullable = False , default = 'default.jpg')
    # photo = db.Column(db.Text, nullable=False)

    def __init__(self, name, amount, summary, created_by, image_file):
        self.name       = name
        self.amount  = amount
        self.summary      = summary
        self.created_by = created_by
        self.image_file = image_file

    # def __repr__(self):
    #     return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 
