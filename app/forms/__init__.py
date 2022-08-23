from tkinter.tix import INTEGER
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Iniciar sesión')


class IngresarPersonalForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    apellido = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    telefono = StringField('Telefono', validators=[])
    enviar = SubmitField('Guardar personal')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})


class IngresarIngresoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    apellido = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    dni = StringField('Dni', validators=[DataRequired('Este campo es requerido')])
    fecha = StringField('Fecha', validators=[DataRequired('Este campo es requerido')])
    motivo = StringField('Motivo', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Guardar ingreso')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})
