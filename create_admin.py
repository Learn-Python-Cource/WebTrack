import sys
from getpass import getpass

from service.app import create_app
from service.models import User, db

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя: ')

    if User.query.filter(User.username==username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password1 = getpass('Введите пароль:')
    password2 = getpass('Введите пароль:')

    if password1 != password2:
        print('Введенные пароли различаются')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.insert_password(password2)

    db.session.add(new_user)
    db.session.commit()

    print('Добавлен новый пользователь {0} id={1}'.format(new_user.username, new_user.id))
