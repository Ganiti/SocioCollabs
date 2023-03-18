from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
	name        = StringField  (u'Name'      )
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])
	email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])

class FundraiserForm(FlaskForm):
	name    = StringField  (u'Name'  , validators=[DataRequired()])
	amount    = StringField(u'Amount'  , validators=[DataRequired()])
	summary    = StringField  (u'Summary'  , validators=[DataRequired()])
	created_by    = StringField  (u'CreatedBy'  , validators=[DataRequired()])

class DonationForm(FlaskForm):
	name_dn            = StringField  (u'Name'  , validators=[DataRequired()])
	fundraiser_name    = StringField  (u'Fundraiser_name'  , validators=[DataRequired()])
	amount             = StringField  (u'Amount'  , validators=[DataRequired()])