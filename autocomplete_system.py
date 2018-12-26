"""
Author: Uchenna Edeh
Comment: I know there is another way to use binary threes for this(tries). We would explore later

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

Example, given the query string de and set of strings [ dog, deer, deal] return [deer, deal].

Hint: Try preprocessing the dictionary into more efficient data structure to speed up queries
"""
import sys

def solution1(my_set, my_string):
    results = preprocess(my_set) 
    return results.get(my_string, None)

def preprocess(my_set):
    results = dict()
    for word in my_set:
        # take first character of first word in array, and build dictionary indexed by first character,
        # increment to second char, do the same indexing, after finishing with current word move to the next
        # at the end you will have a of unique keys with value equivalent to list of all matching words
        
        index_characters(word, results, my_set) 
    return results

def index_characters(word, results, my_set):
    for i in range(len(word)):
        character = word[:i+1]
        if not results.get(character, False):
            results[character] = []
            for mys in my_set:
                if mys.startswith(character):
                    results[character].append(mys) 
            
    

def main(args):
    if len(args) != 3:
        raise AssertionError("Usage:\n\t{0} {1} '{2}' '{3}'\n\tExpected Result: {4}\n\tPlease Try Again!\n\t".format('python3', __file__, 'dog,deer,deal', 'de', 'deer,deal' ))
    print(solution1(args[1].split(','), args[2]))
    #print(solution2([int(x) for x in args[1].split(',')]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(0)

