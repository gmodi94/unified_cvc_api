from flask_sqlalchemy import SQLAlchemy
from src.main import app

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://rapid:Rapid@21@rutvejwaghela.com/rapid"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/rapid"
db = SQLAlchemy(app) 

