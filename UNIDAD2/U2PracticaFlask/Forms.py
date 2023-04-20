from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')

class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    precio = FloatField('Precio', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')


class PaqueteriaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    direccion = StringField('Direccion', validators=[DataRequired()])
    Enviar = SubmitField('Enviar')
    