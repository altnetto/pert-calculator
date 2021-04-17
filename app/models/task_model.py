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
    editing = db.Column(db.Boolean, nullable = False, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    

    def __init__(self, name, critical, optmist, most_probable, pessimist):

        self.name = name
        self.critical = critical
        self.optmist = optmist
        self.most_probable = most_probable
        self.pessimist = pessimist
        self.expected_time = self.calculate_expected()
        self.standard_deviation = self.calculate_standard_deviation()
        self.variance = self.calculate_variance()


    def __str__(self):
        return f'Task #{self.id}, Name: {self.name}, Expected Time: {self.expected_time}'

    
    def calculate_expected(self):
        return round((self.optmist + 4*self.most_probable + self.pessimist)/6, 2)

    
    def calculate_standard_deviation(self):
        return round((self.pessimist-self.optmist)/6, 2)

    
    def calculate_variance(self):
        return round(self.standard_deviation**2, 2)