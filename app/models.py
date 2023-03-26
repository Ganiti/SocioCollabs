from app import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(500))

    def __init__(self, user, email, password):
        self.user = user
        self.password = password
        self.email = email

    def __repr__(self):
        return str(self.id) + " - " + str(self.user)

    def save(self):
        db.session.add(self)

        db.session.commit()

        return self


class Fundraisers(db.Model):
    __tablename__ = "Fundraisers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    amount = db.Column(db.Integer)
    summary = db.Column(db.String(64))
    created_by = db.Column(db.String(64))
    

    def __init__(self, name, amount, summary, created_by):
        self.name       = name
        self.amount  = amount
        self.summary      = summary
        self.created_by = created_by
       

    def __repr__(self):
        return str(self.created_by)  
    def save(self):
        db.session.add(self)

        db.session.commit()

        return self

class New_donations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    name = db.Column (db.String(120), nullable=False)
    fundraiser_name=db.Column(db.String(120), nullable=True)
    amount = db.Column (db.Integer, nullable=False)


    def __init__(
        self,
        email,
        name,
        fundraiser_name,
        amount,
    ):
        self.email = email
        self.name=name
        self.fundraiser_name=fundraiser_name
        self.amount = amount

    def __repr__(self):
        return str(self.name + "-" + str(self.amount))

    def save(self):
        db.session.add(self)

        db.session.commit()

        return self
