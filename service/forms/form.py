from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},  # noqa: Q000
    )
    password = PasswordField(
        'Пароль', validators=[DataRequired()], render_kw={"class": "form-control"},  # noqa: Q000
    )
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})  # noqa: Q000
