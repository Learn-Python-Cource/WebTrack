from flask import Blueprint, redirect, render_template, url_for

from service.forms.form import LoginForm

view = Blueprint('login', __name__)


@view.route('/')
def login():
    form = LoginForm()
    title = 'Авторизация'
    return render_template(
        'login.html',
        page_title=title,
        form=form,
    )
