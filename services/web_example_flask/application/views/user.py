from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import (
    current_user, login_required, login_user,
    logout_user, LoginManager)
from ..forms import LoginForm, UserForm
from ..models import User


user = Blueprint('user', __name__)


login_manager = LoginManager()


def setup_lm(app):
    login_manager.init_app(app)


@user.route(
    '/dashboard/users',
    methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            existing_user = User.query.filter(User.email == email).first()
            if existing_user is None:
                user = User(name=name, email=email)
                user.set_password(password)
                user.insert()
                login_user(user)
                return redirect(url_for('dashboard'))
            flash('User already exists')
            return redirect(url_for('user.create_user'))
    return render_template('forms/new_user.html', form=form)


@user.route(
    '/dashboard/login',
    methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter(User.email == email).first()
            if user and user.check_password(password=password):
                login_user(user)
                return redirect(url_for('dashboard'))
        flash('User not found / Incorrect password')
        return redirect(url_for('user.login'))
    return render_template('forms/login.html', form=form)


@user.route(
    '/dashboard/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash('You need to be logged in to access this page')
    return redirect(url_for('user.login'))
