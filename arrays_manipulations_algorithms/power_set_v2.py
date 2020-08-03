"""
Solution propose by Gayle

Solution #1: Recursion
This problem is a good candidate for the Base Case and Build approach. Imagine that we are trying to find allsubsetsofasetlikeS = {a1, a2, • • • , an}.WecanstartwiththeBaseCase.
 Base Case:n = 0.
There isjust one subset of the empty set: {}.
Case:n = 1.
There are two subsets of the set {aJ: {}, {aJ.
Case:n = 2.
There are four subsets of the set {a1 , aJ: {} ,{aJ, {a),{a1 , a2}.
Case:n = 3.
Now here's where things get interesting. We want to find a way of generating the solution for n on the prior solutions.
3 based
Whatisthedifferencebetweenthesolutionforn 3andthesolutionforn = 2?Let'slookatthismore
deeply:
The difference between these solutions is thatP(2) is missing all the subsets containing a3• P(3) - P(2) = {a3}, {a1, a3}, {a2, a3}, {a1, a2, a3}
How can we useP(2) to createP(3)? We can simply clone the subsets inP(2) and add a3 to them: P(2) {} , {a1}, {a2}, {a1, aJ
P(2) + a, = {a3}, {a1, a3}, {a2, a), {a1, a2, a3}
When merged together, the lines above make P(3).
Case:n > 0
Generating P(n) for the general case is just a simple generalization of the above steps. We compute
P (n-1), clone the results, and then add an to each of these cloned sets.
"""

def solve(my_set, index=0):
    all_sub_sets = []
    if len(my_set) == index:
        all_sub_sets.append([])
    else:
        all_sub_sets = solve(my_set, index + 1)
        item = my_set[index]
        more_sub_set = [] 
        for i in all_sub_sets:
            new_sub_set = [] 
            new_sub_set.extend(i) # add all the elements i had b4
            new_sub_set.append(item) # for each element i had before, i need to add new element 
            more_sub_set.append(new_sub_set) # take this new list and add it to my new collection. At the end, for this new index, I would have list with all the previous element added to new elemenet
        all_sub_sets.extend(more_sub_set) # new element created for index + 1 gets added to our super set

    return all_sub_sets

print("Solution is: ", solve(['a', 'b', 'c', 'd', 'e', 'f'])) 


