"""
Based on the article => https://blog.medium.com/what-are-bloom-filters-1ec2a50c68ff
"""

class BloomFilterADS(object):
    def __init__(self):
        self.A = [0*i for i in range(11)]    # ignore i == 0    

    def insert(self, elem):        
            self.A[elem[0]] = 1
            self.A[elem[1]] = 1
            self.A[elem[2]] = 1

    def is_in_set(self, elem):   
        print(elem)     
        return (self.A[elem[0]] and self.A[elem[1]] and self.A[elem[2]]) == True

hash = {
    "cat" : (3,4,10),
    "dog" : (5,2,1),
    "elephant" : (10,6,7),
    "monkey": (10,2,1)   
}

# reverse_hash = {
#     (3,4,10) : "cat",
#     (3,3,1) : "dog",
#     (10,6,7) : "elephant",
#     (10,2,1) : "monkey",
# }

BF = BloomFilterADS()
BF.insert(hash["cat"])
BF.insert(hash["dog"])

print(BF.is_in_set(hash["cat"])) # Should return True
print(BF.is_in_set(hash["elephant"])) # Should return False
print(BF.is_in_set(hash["monkey"])) # False positive
