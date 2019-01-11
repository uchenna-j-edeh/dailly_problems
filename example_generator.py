class Bank(object): # let's create a bank, building ATMs
   crisis = False
   def create_atm(self):
       while not self.crisis:
           yield "$100"


hsbc = Bank()
corner_street_atm = hsbc.create_atm()
print(type(corner_street_atm))
print(dir(corner_street_atm))
print([corner_street_atm.__next__() for cash in range(5)])
