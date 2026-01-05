from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo 
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed 

from flask_login import current_user
from Carblog.models import User 


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    securityQuestion = StringField('Security Question', validators=[DataRequired()])
    securityAnswer = StringField('Security Answer', validators=[DataRequired()])

    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
        

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')

class UpdateUserForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    picture = FileField('Updated Profile Picture',validators=[FileAllowed(['jpg','png'])])
    securityQuestion = StringField('Security Question', validators=[DataRequired()])
    securityAnswer = StringField('Security Answer', validators=[DataRequired()])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
        

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')

# RESET PASSWORD

class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    securityQuestion = StringField('Security Question', validators=[DataRequired()])
    securityAnswer = StringField('Security Answer', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm New Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError('No account found with that email.')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if not user:
            raise ValidationError('No account found with that username.')

    def validate_securityAnswer(self, field):
        user = User.query.filter_by(email=self.email.data, username=self.username.data).first()
        if user and user.securityAnswer.lower() != field.data.lower():
            raise ValidationError('Security answer is incorrect.')

