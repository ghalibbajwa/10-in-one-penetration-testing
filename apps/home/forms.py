from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField
from wtforms.validators import  DataRequired

class TestForm(FlaskForm):
    test_name = StringField('Test Name',
                         id='test_name',
                         validators=[DataRequired()])
    test_url = StringField('Site URL',
                         id='test_url',
                         validators=[DataRequired()])
    
    site_username = StringField('Site Username',
                         id='site_username')
    

    site_password = PasswordField('Site Password',
                             id='site_password',
                            )
    