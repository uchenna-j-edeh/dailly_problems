"""
Given a list of possible overlapping intervals, return a new list of intervals where all overlapping intervals have been merged
The input list is not necessarily ordered in any way.
for example, given [(1,3), (5,8), (4, 10), (20, 25)], you should return [(1,3), (4, 10), (20, 25)]
"""
new_list = []
def merge_intervals(my_list):
    global new_list
    longest_prev_interval = 0
    my_list = sorted(my_list)
    print(my_list)
    # [(1, 3), (4, 10), (5, 8), (20, 25)]
    end = len(my_list)
    i = 0
    
    while (end - 1 - i >= 0):
        import pdb; pdb.set_trace()
        j = i + 1

        if j == end - 1:
            new_list.append(my_list[j])
            break

        t1a, t1b = my_list[i]
        if t1b < longest_prev_interval:
            i = i + 1
            continue


        #t1a, t1b = my_list[i]
        t2a, t2b = my_list[j]
                
        #if t1b < longest_prev_interval:
        #    continue
        if t1b < t2b:
            new_list.append((t1a,t2b))
            i = i + 1 # skipp next one
            longest_prev_interval = t2b
        else:
            new_list.append((t1a, t1b))
            longest_prev_interval = t1b 

        i = i + 1
        print(i)
        print(new_list)
       
        
my_list = [(1,3), (5,8), (4, 10), (20, 25), (25, 30), (28, 31)]
merge_intervals(my_list)
print(new_list)
