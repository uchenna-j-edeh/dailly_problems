"""
print power set
"""

# iterative

def binary_string(n):
    result = ["0", "1"]
    for it in range(2, n):
        new_result = []
        for s in result:
            new_result.append(s + "0")
            new_result.append(s + "1")

        result = new_result
    return result

def binary_string_general_case(n):
    result = ["a", "b", "c", "d"]
    for it in range(2, n):
        new_result = []
        for s in result:
            for i in result:
                new_result.append(s + i)
        result = new_result
    return result

# recursive DFS approach
class BS(object):
    def __init__(self):
        self.collector = []

    def bshelper(self, slate, n):
        if n == 0:
            self.collector.append(slate)
            return 
    
        self.bshelper(slate + "0", n - 1)
        self.bshelper(slate + "1", n - 1)


def bshelper(slate, n):
    if n == 0:
        print(slate)
        return

    bshelper(slate + "0", n - 1)
    bshelper(slate + "1", n - 1)

    #return slate

 

def binary_string_r(n):
    bshelper("", n)

def binary_string_obj(n):
    bs = BS()
    bs.bshelper("", n)
    return bs.collector


print(binary_string(5))
print(binary_string_general_case(4))

