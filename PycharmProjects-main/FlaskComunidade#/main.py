from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ['douglas', 'aline', 'raziel']

app.config['SECRET_KEY'] = '6ac1072916e394a5d28b53a7288d692e'

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/contato')
def contato():
	return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
	return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form_login = FormLogin()
	form_criar_conta = FormCriarConta()

		#Login com sucesso
	if form_login.validate_on_submit() and 'button_submit_login' in request.form:
		#alertas de login
		flash(f'Login com Sucesso no e-mail {form_login.email_login.data}', 'alert-success')
		#redirecionar para tela principal
		return redirect(url_for('home'))

		#conta com sucesso
	if form_criar_conta.validate_on_submit() and 'button_submit_criar' in request.form:
	# alertas de login
		flash(f'Conta criada com Sucesso no e-mail {form_criar_conta.email_criar.data}', 'alert-success')
	# redirecionar para tela principal
		return redirect(url_for('home'))

	return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)

if __name__ == '__main__':
	app.run(debug=True)