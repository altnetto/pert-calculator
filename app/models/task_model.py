from app.app import db

class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False, default = f'Act{id}')
    critical = db.Column(db.Boolean, nullable = False, default = False)
    optmist = db.Column(db.String(10), nullable = False)
    most_probable = db.Column(db.String(10), nullable = False)
    pessimist = db.Column(db.String(10), nullable = False)
    expected_time = db.Column(db.String(10), nullable = False)
    standard_deviation = db.Column(db.String(10), nullable = False)
    variance = db.Column(db.String(10), nullable = False)

    def __init__(self, name, critical, optmist, most_probable, pessimist):
        self.name = name
        self.critical = critical
        self.optmist = optmist
        self.most_probable = most_probable
        self.pessimist = pessimist
        self.expected_time = (self.optmist + 4*self.most_probable + self.pessimist)/6
        self.standard_deviation = (self.pessimist-self.optmist)/6
        self.variance = self.standard_deviation**2


    def __str__(self):
        return f'Task #{self.id}, Name: {self.name}, Expected Time: {self.expected_time}'