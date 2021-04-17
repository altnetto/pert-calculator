from app.app import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    tasks = db.relationship('TaskModel', backref = 'user', lazy = True)


    def __init__(self, username):
        self.username = username