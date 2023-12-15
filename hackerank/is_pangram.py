"""
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Example

The string contains all letters in the English alphabet, so return pangram.

Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):

string s: a string to test
Returns

string: either pangram or not pangram
Input Format

A single line with string .

Constraints


Each character of , 

Sample Input

Sample Input 0

We promptly judged antique ivory buckles for the next prize

Sample Output 0

pangram

Sample Explanation 0

All of the letters of the alphabet are present in the string.

Sample Input 1

We promptly judged antique ivory buckles for the prize

Sample Output 1

not pangram

Sample Explanation 0

The string lacks an x.
"""

def pangrams(s):
    # Write your code here
    alpha = dict(
        a=0,
        b=0,
        c=0,
        d=0,
        e=0,
        f=0,
        g=0,
        h=0,
        i=0, 
        j=0, 
        k=0, 
        l=0, 
        m=0, 
        n=0, 
        o=0, 
        p=0, 
        q=0, 
        r=0, 
        s=0, 
        t=0, 
        u=0, 
        v=0, 
        w=0,
        x=0,
        y=0,
        z=0,
    )
    
    for ch in s:
        if ch != ' ':
            alpha[ch.lower()] += 1
        
    for a in alpha:
        if not alpha[a]:
            return 0
            
    return 1


print(pangrams("We promptly judged antique ivory buckles for the next prize"))