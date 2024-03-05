from flask_login import UserMixin
from datetime import datetime

from apps import db

class Configs(db.Model, UserMixin):

    __tablename__ = 'Configs'

    id = db.Column(db.Integer, primary_key=True)
    config_name = db.Column(db.String(225), unique=True)
    config_endpoint = db.Column(db.String(225), unique=False)
    config_api_key = db.Column(db.String(225), unique=False, default=None)
    config_username = db.Column(db.String(225), unique=False,default=None)
    config_password = db.Column(db.String(225), unique=False,default=None)
    config_path = db.Column(db.String(225), unique=False,default=None)
    status = db.Column(db.String(225), unique=False,default="In Progress")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

   
    def __repr__(self):
       
        return str(self.config_name)
    





    

