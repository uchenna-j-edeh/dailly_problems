"""
Three way partion algo
input:  [R, B, G, R, B, G, R]
output: [R, R, R. G, G, B, B]
"""


def dutch_flag(clist):
    lo = 0
    hi = len(clist) - 1
    i = 0

    while i <= hi:
        if clist[i] == 'R':
            clist[lo], clist[i] = clist[i], clist[lo] # swap
            lo = lo + 1
            i = i + 1
        elif clist[i] == 'B':
            clist[hi], clist[i] = clist[i], clist[hi] # swap
            hi = hi - 1
        else:
            i = i + 1

    return clist


arr = [
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R',
    'R', 'B', 'G', 'R', 'B', 'G', 'R','R', 'B', 'G', 'R', 'B', 'G', 'R'
    ]

print(dutch_flag(arr))

arr = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']
print(dutch_flag(arr))

print(dutch_flag(['R', 'R']))
