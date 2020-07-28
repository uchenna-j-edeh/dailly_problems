"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)
"""

def solve(my_str):
    counter = {}
    for i in my_str:
        j = i.lower()

        if i == ' ':
            continue

        if counter.get(j, False):
            counter[j] = counter[j] + 1
        else:
            counter[j] = 1

    odd_found = False
    print(counter)
    for k,v in counter.items():
        is_even = v % 2 == 0

        if not is_even:
            if odd_found:
                return False, k
            odd_found = True
        
    return True

print("The solution is :", solve('Tact Coa'))
print("The solution is :", solve('tactcoapapa'))
print("The solution is :", solve('Uchenna'))
