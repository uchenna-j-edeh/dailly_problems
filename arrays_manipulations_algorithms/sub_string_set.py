"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.
for example, given the string "figehaeci" and a set of caracters {a, e, i}, you should return aeci. 
if there is no substring containing all the characters return null.
strategy: precompute the cumulative ord values, the take a slice of the substring equal the the length of the set and compare, repeat
"""
def check_sub_str(mtext, mlist):
    """_summary_

    Args:
        mtext (_type_): _description_
        mlist (_type_): _description_

    Returns:
        _type_: _description_
    """
    shortest_sub_str = mtext
    mdict = {}
    for s in mlist:
        mdict[s] = 1

    for i in range(len(mtext)):
        if mdict.get(mtext[i], False):
            new_mdict = dict()
            new_mdict[mtext[i]] = 1

            for j in range(i+1, len(mtext)):
                if mdict.get(mtext[j], False):
                    new_mdict[mtext[j]] = 1

                if mdict.get(mtext[j], False) and len(new_mdict) == len(mdict):
                    if len(mtext[i:j+1]) < len(shortest_sub_str):
                        shortest_sub_str = mtext[i:j+1]
                        break
                

    return shortest_sub_str


print(check_sub_str("figehaeci", ['a','e', 'i']))

