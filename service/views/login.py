from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from service.forms.form import LoginForm
from service.models import User

view = Blueprint('login', __name__)


@view.route('/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('weather.index'))
    form = LoginForm()
    title = 'Авторизация'
    return render_template(
        'login.html',
        page_title=title,
        form=form,
    )


@view.route('/handler', methods=['POST'])
def login_handler():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('news.py_news'))
    flash('Не правильное имя пользователя или пароль')
    return redirect(url_for('login.login'))


@view.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('weather.index'))
