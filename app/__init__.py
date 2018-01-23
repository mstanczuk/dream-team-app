from flask import Flask


#initialize app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

from app import views