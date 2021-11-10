from models import db

class transcation_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_id = db.Column(db.String,nullable=True)
    to_id = db.Column(db.String)
    status = db.Column(db.String)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())