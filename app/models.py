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
    #image_file = db.Column(db.String(20), nullable = False , default = 'default.jpg')
    # photo = db.Column(db.Text, nullable=False)

    def __init__(self, name, amount, summary, created_by):
        self.name       = name
        self.amount  = amount
        self.summary      = summary
        self.created_by = created_by
        #self.image_file = image_file

    def __repr__(self):
        return str(self.created_by)  # + '-' + str(self.amount)

    def save(self):
        db.session.add(self)

        db.session.commit()

        return self


class Donations(db.Model):
    __tablename__ = "Donations"

    id = db.Column(db.Integer, primary_key=True)
    name_dn = db.Column(db.String(64))
    fundraiser_name = db.Column(db.String(64))
    amount = db.Column(db.Integer)

    def __init__(
        self,
        name_dn,
        fundraiser_name,
        amount,
    ):
        self.name_dn = name_dn
        self.fundraiser_name = fundraiser_name
        self.amount = amount

    def __repr__(self):
        return str(self.name_dn) + "-" + str(self.amount)

    def save(self):
        db.session.add(self)

        db.session.commit()

        return self
