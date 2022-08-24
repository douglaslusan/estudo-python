from flask_wtf import FlaskForm
from flask_wtf.file import FileField, file_allowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
	username_criar = StringField('Username', validators=[DataRequired()])
	email_criar = StringField('E-mail', validators=[DataRequired(), Email()])
	password_criar = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
	confirm_criar = PasswordField('Password confirm', validators=[DataRequired(), EqualTo('password_criar')])
	button_submit_criar = SubmitField('Enviar')

	#obrigatorio nome validate junto com a variavel(CAMPO)
	def validate_email_criar(self, email):
		usuario = Usuario.query.filter_by(email=email.data).first()
		if usuario:
			raise ValidationError('email já cadastrado')


class FormLogin(FlaskForm):
	email_login = StringField('E-mail', validators=[DataRequired(), Email()])
	password_login = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
	remember_login = BooleanField('Remember Login')
	button_submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
	username_editar = StringField('Username', validators=[DataRequired()])
	email_editar = StringField('E-mail', validators=[DataRequired(), Email()])
	foto = FileField('Atualizar foto de perfil',validators=[file_allowed(['jpg', 'png'])])
	curso_excel = BooleanField('Excel')
	curso_powerBI = BooleanField('Power BI')
	curso_Python = BooleanField('Python')
	curso_vba = BooleanField('VBA')
	curso_ppt = BooleanField('Apresentacao')
	curso_sql = BooleanField('Sql')
	curso_javascript = BooleanField('JavaScript')
	curso_cSharp = BooleanField('C#')
	curso_C = BooleanField('C')

	button_submit_editar = SubmitField('Save')


	def validate_email_criar(self, email):
		#verificar se o usuario modificou o email
		if current_user.email_login != email.data:
			usuario = Usuario.query.filter_by(email=email.data).first()
			if usuario:
				raise ValidationError('email já cadastrado')


class FormCriarPost(FlaskForm):
	titulo = StringField('Titulo', validators=[DataRequired(), Length(2, 30)])
	corpo = TextAreaField('Escreva seu Post', validators=[DataRequired()])
	button_submit = SubmitField('Criar Post')