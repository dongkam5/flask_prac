from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,EmailField
from wtforms import validators,ValidationError


class ContactForm(Form):
    name = StringField('Name of Student', [validators.DataRequired('Please enter your name')])
    gender = RadioField('Gender',choices=[('M','Male'),('F','Female')])
    address=TextAreaField('Address')
    email=EmailField('Email', [validators.DataRequired('Please enter your email address')])
    age = IntegerField('Age')
    language=SelectField('Language',choices=[('cpp','C++'),('py','python')])
    submit=SubmitField('Send')

#, [validators.DataRequired('Please enter your name')]
# ,[validators.DataRequired('Please enter your email address')]