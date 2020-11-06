"""
You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour. Implement a data structure that efficiently supports the following:

update(hour: int, value: int): Increment the element at index hour by value.
query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).
You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end values that wrap around midnight.
"""

class Manager(object):
    def __init__(self, A):
        self.A = [-1] + A#= [i*0 for i in range(25)]        
        
    def validation(self, value):
        if value < 1 or value > 24:
            return False
        return True

    def update(self, hour, value):       
        if self.validation(hour):
            self.A[hour] += value
        else:
            raise ValueError("An hour must be between 1 and 24 inclusive...")        

    def query(self, start, end):   
        if self.validation(start) and self.validation(end):     
            return sum(self.A[start: end+1])
        else:
            raise ValueError("An hour must be between 1 and 24 inclusive...")

A = [10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 500, 0, 0, 0, 0, 0, 0]
man = Manager(A)
man.update(1,10)
man.update(2,5)
man.update(12, 100)
man.update(18, 500)

print(man.A)

print(man.query(1, 24))
    

        