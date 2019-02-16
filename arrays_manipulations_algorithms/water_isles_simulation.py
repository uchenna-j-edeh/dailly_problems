"""
write a function that receives a position in 2 dimentions (x, y) array, which
was intially initialized with 'o' (signals 'water'), the function changes the value/state of that position
 to 'x' (signals 'land') and returns the number of isles in the board
for example, for 3x3 board, it will initially look like the following:
    o o o
    o o o
    o o o
After calling the function with the position (1, 2), the board will look like:
    o o x
    o o o
    o o o
and returns 1.
An isle is defined as 'x' surrounded horizontally and vertically with 'o' in the
following board there is only one isle:
    o o o
    o x x
    o x o
"""
from pprint import pprint as pp

def set_values(arr_nd, x, y):
    for i, arr in enumerate(arr_nd):
        for j, val in enumerate(arr):
            if i == x and j == y:
                arr[j] = 'x'
                return 1
            

def find_all_isles(arr_nd):
    all_isles = []
    for i, arr in enumerate(arr_nd):
        for j, val in enumerate(arr):
            #import pdb; pdb.set_trace()
            #print(arr_nd[i][j])
            if i > 0 and i + 1 < len(arr_nd) and arr_nd[i-1][j] == 'o' and arr_nd[i+1][j] == 'o' and arr_nd[i][j] == 'x':
                #print(arr_nd[i][j])
                print(i,j)
                all_isles.append('{0},{1}'.format(i, j))
    return all_isles

arrs = [
    ['o', 'o', 'o'],
    ['o', 'o', 'o'],
    ['o', 'o', 'o']
]

set_values(arrs, 1, 1)
set_values(arrs, 2, 1)
set_values(arrs, 1, 2)

pp(arrs)

find_all_isles(find_all_isles(arrs))

#pp(arrs)




