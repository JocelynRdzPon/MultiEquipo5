from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PersonalForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')

class OficinaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    direccion = StringField('Direccion', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')

class TituloForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')

class AreaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')

class CargoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')