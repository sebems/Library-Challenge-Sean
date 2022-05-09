import random

class Student:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        
        self.id = random.randrange(1, 100)

    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)