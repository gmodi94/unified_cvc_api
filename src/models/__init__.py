from flask_sqlalchemy import SQLAlchemy
from src.main import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rduyhaijhswewi:ae48d038f00869949241ae4aae2cde0896d47a8f40da61fc529f5c06504e3d95@ec2-107-20-127-127.compute-1.amazonaws.com:5432/dftfh0bgikn7rr"
db = SQLAlchemy(app) 

