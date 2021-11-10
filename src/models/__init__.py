from flask_sqlalchemy import SQLAlchemy
from main import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:postgres@localhost:5432/rapid"


