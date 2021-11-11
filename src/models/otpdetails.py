from src.models import db

class otp_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    otp_data = db.Column(db.String,nullable=True)
    mobile_number = db.Column(db.String(50))