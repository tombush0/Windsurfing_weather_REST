from flask import Flask

from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = "not so secret"
app.config['WTF_CSRF_ENABLED'] = False
config = Config()

from app.Requests import routes
