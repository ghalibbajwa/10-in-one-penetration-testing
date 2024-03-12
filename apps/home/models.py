from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from apps import db


class Tests(db.Model, UserMixin):

    __tablename__ = 'Tests'

    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(225), unique=False)
    test_url = db.Column(db.String(225), unique=False)
    site_username = db.Column(db.String(225), unique=False)
    status = db.Column(db.String(225), default="Running", unique=False)
    site_password = db.Column(db.String(225), unique=False)
    burp_id = db.Column(db.Integer, nullable=True)
    burp_data = db.Column(JSON, nullable=True)
    zap_data = db.Column(JSON, nullable=True)
    zap_id = db.Column(db.Integer, nullable=True)

    nuclei_data = db.Column(JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



    def __repr__(self):
        return str(self.test_name)

