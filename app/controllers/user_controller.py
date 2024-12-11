from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from app.services.user_service import UserService
from infrastructure.user_db.sqlite_user_repository import SQLiteUserRepository


# Configurar el servicio de usuario
repository = SQLiteUserRepository('users.db')
user_service = UserService(repository)

# Registrar el blueprint
user_blueprint = Blueprint('users', __name__)

# Ruta para la página de login
@user_blueprint.route('/login', methods=['GET'])
def render_login_form():
    if 'user_id' in session:
        return redirect(url_for('movie.index')) 
    return render_template('users/login.html')

# Ruta para el login en base a funcionalidades 
@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session: 
        return redirect(url_for('movie.index')) 

    if request.method == 'POST':
        data = request.form
        email = data['email']
        password = data['password']

        user = user_service.validate_user(email, password)
        if user:
            session['user_id'] = user.id
            session['user_name'] = user.name
            return redirect(url_for('movie.index'))
        else:
            flash('Credenciales inválidas', 'danger')
            return redirect(url_for('users.render_login_form'))

    return render_template('login.html')


# Ruta para cerrar sesión
@user_blueprint.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('Has cerrado sesión exitosamente', 'info')
    return redirect('/users/login')
 
# Ruta para la página de registro
@user_blueprint.route('/register', methods=['GET'])
def render_register_form():
    if 'user_id' in session:
        return redirect(url_for('movie.index'))
    return render_template('users/register.html')

# Ruta para el registro de usuarios en base a funcionalidades
@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data['name']
    email = data['email']
    password = data['password']

    if user_service.get_user_by_email(email):
        flash('El correo electrónico ya está en uso', 'warning')
        return redirect(url_for('users.render_register_form'))

    user_service.create_user(name, email, password)
    flash('Registro exitoso, por favor inicia sesión', 'success')
    return redirect(url_for('users.render_login_form'))

