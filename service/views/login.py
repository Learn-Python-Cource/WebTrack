from flask import Blueprint, redirect, render_template, url_for

view = Blueprint('login', __name__)


@view.route('/')
def login():
    pass
