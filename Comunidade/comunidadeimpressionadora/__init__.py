from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY' ] = '6ac1072916e394a5d28b53a7288d692e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #funcao para enviar para a pagina de login quando nao está logado (login_required)
login_manager.login_message_category = 'alert-warning'

from comunidadeimpressionadora import routes
