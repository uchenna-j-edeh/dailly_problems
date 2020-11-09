
class CircleADT(object):
    def __init__(self):
        self.arr = [i for i in range(70)]
        self.curr_index = 0

    def add_elem(self, val):
        if self.curr_index == len(self.arr):
            self.curr_index = 0
        self.arr[self.curr_index] = val
        self.curr_index += 1

def circular(limit=1000000):    
    count = 0
    CDT = CircleADT()    
    while count < limit:
        CDT.add_elem(count)
        count += 1

    return CDT.arr

print(circular())
print("\n")
print(circular(100))
print(circular(70))