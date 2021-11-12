from flask_sqlalchemy import SQLAlchemy
from src.main import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://loudtsfzmqobmn:36a3d46f18640439a1bbed8dbd730a29a7fc97852130b59f1fb4ea846a662925@ec2-107-23-213-65.compute-1.amazonaws.com:5432/ddn63kvo42m0er"
db = SQLAlchemy(app) 

