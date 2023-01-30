from math import ceil

def finalInstances(instances, averageUtil): 
    # Write your code here
    current = instances
    c = 0
    while c < len(averageUtil):
        print(averageUtil[c])
        if averageUtil[c] >=  25 and averageUtil[c] <= 60: # 25
            c = c + 1
        elif averageUtil[c] < 25: # 23
            current = ceil(current/2)
            c = c + 11
            print('b'+ repr(current))
        else: # averageUtil[c] > 60:
            current = ceil(current * 2)
            print('a'+ repr(current))
            c = c + 11
    return current

instances = 2
averageUtil = [25,23,1,2,3,4,5,6,7,8,9,10,76,80]
print(finalInstances(instances, averageUtil))