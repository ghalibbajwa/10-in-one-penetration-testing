from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField
from wtforms.validators import  DataRequired

class BurpForm(FlaskForm):
    config_name = StringField('Name',
                         id='config_name',
                         default="Burp Suite",
                        )
    
    config_endpoint = StringField('Endpoint',
                         id='config_endpoint',
                         validators=[DataRequired()])
    
    config_api_key = StringField('API Key',
                         id='config_api_key',
                         validators=[DataRequired()])
    

class NessusForm(FlaskForm):
    config_name = StringField('Name',
                         id='config_name',
                         default="Nessus",
                        )
    
    config_endpoint = StringField('Endpoint',
                         id='config_endpoint',
                         validators=[DataRequired()])
    
    config_username = StringField('Nessus Username',
                         id='config_username',
                         validators=[DataRequired()])
    

    config_password = PasswordField('Nessus Password',
                             id='config_password',
                            )
    

class NucleiForm(FlaskForm):
    config_name = StringField('Name',
                         id='config_name',
                         default="Nuclei",
                        )
    
    config_path = StringField('Nuclei Path',
                         id='config_path',
                         validators=[DataRequired()])
    


class ZapForm(FlaskForm):
    config_name = StringField('Name',
                         id='config_name',
                         default="Zap",
                        )
    
    config_endpoint = StringField('Endpoint',
                         id='config_endpoint',
                         validators=[DataRequired()])
    
    config_api_key = StringField('API Key',
                         id='config_api_key',
                         validators=[DataRequired()])


class ConfigForm(FlaskForm):
    config_name = StringField('Name',
                         id='config_name',
                         validators=[DataRequired()],
                        )
    
    config_endpoint = StringField('Endpoint',
                         id='config_endpoint',
                         )
    
    config_api_key = StringField('API Key',
                         id='config_api_key',
                        )
    
    config_path = StringField('Binary Path',
                         id='config_path',
                         )
    
    config_username = StringField('Nessus Username',
                         id='config_username',
                         )
    

    config_password = PasswordField('Nessus Password',
                             id='config_password',
                            )