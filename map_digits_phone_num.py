"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all
possible letterss the number could represent. You can assume each vlid number in the mapping is 
a single digits

For example if {"2": ["a", "b", "c"], "3": ["d", "e", "f"],...} then "23" should return ["ad", 'ae", "af", 
"bd", "be", "bf", "cd", "ce", "f"].
"""

def solution1(my_dict, num):
    len_num = len(num)
    _lists = []
    for i, v1 in enumerate(num):
        _lists.append(my_dict[v1])

    #print(_lists[0]) 
    results = []
    for i, v1 in enumerate(_lists[0]):
        #print ('v1 =>', i, v1)
        #print(i+1)
       
        #for j in range(i+1 < len(_lists)):
        #    result = ''
        #    for k in _lists[j]:
        #    print ('k =>', _lists[k])
        #        result = result + v1 + k 
        #    print( result)
        #print (result) 
        result = v1
        #mset = set()
        #print( v1)
        #mset.add(v1)
        mlist=[v1]
        #for t in range(len(_lists[0])):
        #    mlist=[v1]
        for j in range(1, len(_lists)): # (1)
            #result = v1 + _lists[j][i] # 
            #result = result + v1 + _lists[j][i]
            #mset.add(_lists[j][i])
            mlist.append(_lists[j][i])
   
        print(''.join(mlist)) 
        #print(mset) 


my_dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"]}
#my_dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"]}
#num = "234"
num = "23"
print(solution1(my_dict, num))
