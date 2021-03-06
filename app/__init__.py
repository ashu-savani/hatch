from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
Bootstrap(app)
from flask_login import UserMixin


from app import routes, models
