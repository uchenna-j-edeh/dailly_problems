def matchingStrings(strings, queries):
    # Write your code here
    mhash = {}
    results = []
    # for q in queries:
    #     mhash[q] = 0
        
    for s in strings:
        if mhash.get(s, False):
            mhash[s] += 1
        else:
            mhash[s] = 1
    
    for q in queries:
        if mhash.get(q, False):
            results.append(mhash[q])
        else:
            results.append(0)
        
    return results


strings = ['ab', 'ab', 'abc']
queries = ['ab','abc', 'bc']

print(matchingStrings(strings, queries))