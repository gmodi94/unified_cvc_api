from src.models import db

class transcation_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_id = db.Column(db.String(250),nullable=True)
    to_id = db.Column(db.String(250))
    status = db.Column(db.String(250))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())