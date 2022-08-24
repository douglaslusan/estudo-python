from flask import render_template, redirect, url_for, flash, request, abort
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from comunidadeimpressionadora.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image


@app.route('/')
def home():
	posts = Post.query.order_by(Post.id.desc())
	return render_template('home.html', posts=posts)


@app.route('/contato')
def contato():
	return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
	lista_usuarios = Usuario.query.all()
	return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form_login = FormLogin()
	form_criar_conta = FormCriarConta()

	# Login com sucesso
	if form_login.validate_on_submit() and 'button_submit_login' in request.form:
		# verificar se ja existe usuario e checar senha
		usuario = Usuario.query.filter_by(email=form_login.email_login.data).first()
		if usuario and bcrypt.check_password_hash(usuario.password, form_login.password_login.data):
			login_user(usuario, remember=form_login.remember_login.data)
			# alertas de login
			flash(f'Login com Sucesso no e-mail {form_login.email_login.data}', 'alert-success')
			param_next = request.args.get('next')
			if param_next:
				return redirect(param_next)
			else:
				# redirecionar para tela principal
				return redirect(url_for('home'))
		else:
			flash(f'Username ou password Inválidos {form_login.email_login.data}', 'alert-danger')

	# conta com sucesso
	if form_criar_conta.validate_on_submit() and 'button_submit_criar' in request.form:
		# criptografar senha
		password_cript = bcrypt.generate_password_hash(form_criar_conta.password_criar.data)
		# criar o usuario
		usuario = Usuario(username=form_criar_conta.username_criar.data,
						  email=form_criar_conta.email_criar.data,
						  password=password_cript)
		# adicionar sessao
		database.session.add(usuario)
		# commit na sessao
		database.session.commit()

		# alertas de login
		flash(f'Conta criada com Sucesso no e-mail {form_criar_conta.email_criar.data}', 'alert-success')
		# redirecionar para tela principal
		return redirect(url_for('home'))

	return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash(f'Logout efetuado', 'alert-success')
	return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
	foto = url_for('static', filename='image/{}' .format(current_user.foto))
	return render_template('perfil.html', foto=foto)


@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
	form = FormCriarPost()
	if form.validate_on_submit():
		post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
		database.session.add(post)
		database.session.commit()
		flash('Post criado com sucesso', 'alert-success')
		return redirect(url_for('home'))
	return render_template('criar_post.html', form=form)


def salvar_imagem(imagem):
	# adicionando nome aleatorio na imagem
	codigo = secrets.token_hex(8)
	nome, extensao = os.path.splitext(imagem.filename)
	nome_arquivo = nome + codigo + extensao
	# reduzindo o tamanho da imagem
	tamanho = (200, 200)
	imagem_reduzida = Image.open(imagem)
	imagem_reduzida.thumbnail(tamanho)
	# salvar a imagem na pasta fotos_perfil
	caminho_completo = os.path.join(app.root_path, 'static/image', nome_arquivo)
	imagem_reduzida.save(caminho_completo)
	return nome_arquivo


def atualizar_cursos(form):
	lista_curso = []
	for campo in form:
		if 'curso_' in campo.name:
			# adicionar o texto do campo.label
			if campo.data:
				lista_curso.append(campo.label.text)

	return ';'.join(lista_curso)


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
	form = FormEditarPerfil()
	if form.validate_on_submit():
		current_user.email = form.email_editar.data
		current_user.username = form.username_editar.data
		if form.foto.data:
			nome_imagem = salvar_imagem(form.foto.data)
			# modificando o campo foto do usuario para o novo nome da imagem
			current_user.foto = nome_imagem
		current_user.curso = atualizar_cursos(form)
		database.session.commit()
		flash(f'Conta modificada com Sucesso', 'alert-success')
		return redirect(url_for('perfil'))
	elif request.method == 'GET':
		form.email_editar.data = current_user.email
		form.username_editar.data = current_user.username

	foto = url_for('static', filename='image/{}'.format(current_user.foto))
	return render_template('editarperfil.html', foto=foto, form=form)


@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def	exibir_post(post_id):
	post = Post.query.get(post_id)
	if current_user == post.autor:
		form = FormCriarPost()
		if request.method == 'GET':
			form.titulo.data = post.titulo
			form.corpo.data = post.corpo
		elif form.validate_on_submit():
			post.titulo = form.titulo.data
			post.corpo = form.corpo.data
			database.session.commit()
			flash('Post atualizado com suceeso', 'alert-success')
			return redirect(url_for('home'))
	else:
		form = None
	return render_template('post.html', post=post, form=form)


@app.route('/post/<post_id>/excluir', methods=['GET', 'POST'])
@login_required
def excluir_post(post_id):
	post = Post.query.get(post_id)
	if current_user == post.autor:
		database.session.delete(post)
		database.session.commit()
		flash('Post Excluido', 'alert-danger')
		return redirect(url_for('home'))
	else:
		abort(403)

