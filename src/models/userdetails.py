from src.models import db

class UserDetails(db.Model):
    __tablename__ = 'user_details'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    mobile_number = db.Column(db.String(250))
    email = db.Column(db.String(250))
    extra_notes = db.Column(db.String(250))
    address = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    jwt_tokens = db.Column(db.String(250), nullable =True)
    blob_file = db.Column(db.Text,nullable =True)