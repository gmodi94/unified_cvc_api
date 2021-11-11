from flask_sqlalchemy import SQLAlchemy
from src.main import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://xyjlmjsvjiydbr:c7e5b50a48bc3703459b8aa06ad2f11b1a00a3d276d5ffbf753aecf09c4b9469@ec2-107-20-127-127.compute-1.amazonaws.com:5432/d1pff5530s4t7d"
db = SQLAlchemy(app) 

