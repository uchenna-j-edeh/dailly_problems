"""
Author: Uchenna Edeh
Given an unsorted arrays of integers, find the length of the longest
consecutive elements sequence.

Example, given [ 100, 4, 200, 1, 3, 2]. the longest consecutive sequesnce is
[1, 2, 3, 4], length 4.
Question: Can elements be repeated? Assume NO.
"""
def longest_sequence(mylist):
    # first store all the elements in a hash map.

    my_hash = dict()
    for i in mylist:
        if my_hash.get(i, False):
            my_hash[i] = my_hash[i] + 1
        else:
            my_hash[i] = 1

    
    longest_seq = []
    for val in (mylist):
        seq = []
        if my_hash.get(val - 1, False): # if there is a lower value skip
            continue

        #seq.append(val)
        count = 0
        while True:
            if my_hash.get(val + count, False)
                seq.append(val)
            else:
                break
            count = count + 1 

        if len(seq) > len(longest_seq):
            longest_seq = seq

    return longest_seq

print(longest_sequence([ 100, 4, 200, 1, 3, 2]))
                
                
            
