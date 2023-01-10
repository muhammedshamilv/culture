from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import app
import settings
username = settings.username
password = settings.password
dbname = settings.dbname


app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://%s:%s@localhost/%s'%(username,password,dbname)
db = SQLAlchemy(app)
from models import experience_template