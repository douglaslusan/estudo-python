from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
	username_criar = StringField('Username', validators=[DataRequired()])
	email_criar = StringField('E-mail', validators=[DataRequired(), Email()])
	password_criar = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
	confirm_criar = PasswordField('Password confirm', validators=[DataRequired(), EqualTo('password')])
	button_submit_criar = SubmitField('Enviar')

class FormLogin(FlaskForm):
	email_login = StringField('E-mail', validators=[DataRequired(), Email()])
	password_login = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
	remember_login = BooleanField('Remember Login')
	button_submit_login = SubmitField('Login')
