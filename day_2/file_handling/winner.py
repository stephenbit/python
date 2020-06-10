class Winner:

    def __init__(self, index, year, age, name, movie):
        self.index = index
        self.year = year
        self.age = age
        self.name = name
        self.movie = movie

    def values(self):
        return [self.index, self.year, self.age, self.name, self.movie]
