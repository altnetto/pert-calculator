class GausModel(db.Model):
    def __init__(self, range, min, exp, max):
        self.range = range
        self.min = min
        self.exp = exp
        self.max = max

    
    