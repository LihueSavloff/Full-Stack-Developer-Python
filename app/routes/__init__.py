from flask import render_template, redirect, url_for, session, flash, request
from app.auth import login_required
import logging
logging.basicConfig(level=logging.INFO)
from app import app
from app.forms import LoginForm, IngresarPersonalForm
from app.handlers import validar_usuario, get_personal, get_personal_por_id, agregar_personal, eliminar_personal
from app.forms import IngresarIngresoForm
from app.handlers import get_ingreso, get_ingreso_por_id, agregar_ingreso, eliminar_ingreso

@app.route('/')  # http://localhost:5000/
@login_required
def index():
    if request.method == 'GET' and request.args.get('borrar'):
        eliminar_ingreso(request.args.get('borrar'))
        flash('Se ha eliminado el ingreso', 'success')
    return render_template('index.html', titulo="Ingresos", ingresos=get_ingreso())


@app.route('/ingresar-ingreso', methods=['GET', 'POST'])
@login_required
def ingresar_ingreso():
    ingresar_ingreso_form = IngresarIngresoForm()
    if ingresar_ingreso_form.cancelar.data:  # si se apretó el boton cancelar, ingreso_form.cancelar.data será True
        return redirect(url_for('index'))
    if ingresar_ingreso_form.validate_on_submit():
        datos_nuevos = { 'nombre': ingresar_ingreso_form.nombre.data, 
                         'apellido': ingresar_ingreso_form.apellido.data, 
                         'dni': ingresar_ingreso_form.dni.data, 
                         'fecha': ingresar_ingreso_form.fecha.data, 
                         'motivo': ingresar_ingreso_form.motivo.data }
        agregar_ingreso(datos_nuevos)
        flash('Se ha agregado un nuevo ingreso', 'success')
        return redirect(url_for('index'))
    return render_template('ingresar_ingreso.html', titulo="Alta de ingreso", ingresar_ingreso_form=ingresar_ingreso_form)

@app.route('/editar-ingreso/<int:id_ingreso>', methods=['GET', 'POST'])
@login_required
def editar_ingreso(id_ingreso):
    ingreso_form = IngresarIngresoForm(data=get_ingreso_por_id(id_ingreso))
    if ingreso_form.cancelar.data:  # si se apretó el boton cancelar, ingreso_form.cancelar.data será True
        return redirect(url_for('index'))
    if ingreso_form.validate_on_submit():
        datos_nuevos = { 'nombre': ingreso_form.nombre.data, 
                         'apellido': ingreso_form.apellido.data, 
                         'dni': ingreso_form.dni.data, 
                         'fecha': ingreso_form.fecha.data, 
                         'motivo': ingreso_form.motivo.data}
        eliminar_ingreso(id_ingreso)  # Eliminamos el ingreso antiguo
        agregar_ingreso(datos_nuevos)  # Agregamos el nuevo ingreso
        flash('Se ha editado el ingreso exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('editar_ingreso.html', titulo="Editar ingreso", ingreso_form=ingreso_form)

@app.route('/personal', methods=['GET', 'POST'])
@login_required
def personal():
    if request.method == 'GET' and request.args.get('borrar'):
        eliminar_personal(request.args.get('borrar'))
        flash('Se ha eliminado el empleado', 'success')
    return render_template('personal.html', titulo="Personal", personal=get_personal())


@app.route('/ingresar-personal', methods=['GET', 'POST'])
@login_required
def ingresar_personal():
    personal_form = IngresarPersonalForm()
    if personal_form.cancelar.data:  # si se apretó el boton cancelar, personal_form.cancelar.data será True
        return redirect(url_for('personal'))
    if personal_form.validate_on_submit():
        datos_nuevos = { 'nombre': personal_form.nombre.data, 'apellido': personal_form.apellido.data, 
                         'telefono': personal_form.telefono.data }
        agregar_personal(datos_nuevos)
        flash('Se ha agregado un nuevo empleado', 'success')
        return redirect(url_for('personal'))
    return render_template('ingresar_personal.html', titulo="Personal", personal_form=personal_form)


@app.route('/editar-personal/<int:id_empleado>', methods=['GET', 'POST'])
@login_required
def editar_personal(id_empleado):
    personal_form = IngresarPersonalForm(data=get_personal_por_id(id_empleado))
    if personal_form.cancelar.data:  # si se apretó el boton cancelar, personal_form.cancelar.data será True
        return redirect(url_for('personal'))
    if personal_form.validate_on_submit():
        datos_nuevos = { 'nombre': personal_form.nombre.data, 'apellido': personal_form.apellido.data, 
                         'telefono': personal_form.telefono.data }
        eliminar_personal(id_empleado)  # Eliminamos el empleado antiguo
        agregar_personal(datos_nuevos)  # Agregamos el nuevo empleado
        flash('Se ha editado el empleado exitosamente', 'success')
        return redirect(url_for('personal'))
    return render_template('editar_personal.html', titulo="Personal", personal_form=personal_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        usuario = login_form.usuario.data
        password = login_form.password.data
        if validar_usuario(usuario, password):
            session['usuario'] = usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', titulo="Login", login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))


