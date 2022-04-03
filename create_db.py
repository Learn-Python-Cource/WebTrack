from service import app, models

db = models.db

db.create_all(app=app.create_app())

