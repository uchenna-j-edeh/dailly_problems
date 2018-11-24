class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @full_name.setter
    def full_name(self, value):
         self.first_name, self.last_name = value.split(" ", 1)
