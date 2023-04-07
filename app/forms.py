
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, PasswordField

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired, FileAllowed
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField 
from wtforms.validators import InputRequired, Email, DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])


class FundraiserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    amount = StringField("Amount", validators=[DataRequired()])
    summary = StringField("Summary", validators=[DataRequired()])
    #created_by = StringField("CreatedBy", validators=[DataRequired()])
    
class DonationForm(FlaskForm):
    name_dn = StringField("Name", validators=[DataRequired()])
    fundraiser_name = StringField("Fundraiser_name", validators=[DataRequired()])
    amount = StringField("Amount", validators=[DataRequired()])
    email =  StringField("Email", validators=[DataRequired()])

