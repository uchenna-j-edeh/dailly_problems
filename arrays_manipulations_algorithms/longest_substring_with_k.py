"""
Given an integer k and a substring s, find the length of the longest substring that contains at most k distinc characters
for example, given s = "abcba" and k = 2, then the longest substring with k distinct characters is 'bcb'
"""

#my_str = "abcba"
#k = 2


# "bcb" => has 2 distinct chars
# "abcba" => has 4 distinc chars

def solution(k, my_str):
    begining_length_of_distinct_char = 0 # must be 3 since "bcb" contains 3 chars
    end_length_of_distinct_char = '' # must be 3 since "bcb" contains 3 chars
    number_of_distinc_chars = 0 # must be k. 2 in this example
    mhash = dict()

    for pos, ch in enumerate(my_str):
        pos = pos + 1 # we don't want to use 0 as the value of an indes. It will test to false
        if mhash.get(ch, False):
            mhash[ch] = -1 *  mhash[ch] # flip sign to indicate odd or even
            counter = 2
            if 1 > mhash[ch]:
                counter = 1 

            begining_length_of_distinct_char = abs(mhash[ch])
            number_of_distinc_chars = counter + number_of_distinc_chars
            if number_of_distinc_chars == k:
                # unshift positions
                begining_length_of_distinct_char = begining_length_of_distinct_char - 1
                pos = pos - 1
                return my_str[begining_length_of_distinct_char: pos + 1]
        else: # char is not there
            mhash[ch] = -1 * pos
    return None         

print(solution(2, "abcba"))
print(solution(4, "abcba"))
print(solution(5, "abcbaxa"))
print(solution(9, "givenanintegerkandasubstringdistinccharacters"))
