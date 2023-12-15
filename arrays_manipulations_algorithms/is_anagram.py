# An anagram is a word, a phrase, or a name formed by rearranging the letters of another.
#
# Examples:
#
# "arc" and "car"
# "cinema" and "iceman"
# "a gentleman" and "elegant man"
# "Clint Eastwood" and "old west action"
#
# If I give you 2 strings, can you tell me if they're anagrams of each other?

# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

def is_anagram(str1, str2):

    
    my_dict = {}
    for s in str1:
        s = s.lower()
        if s != ' ':
            if my_dict.get(s, False):
                my_dict[s] +=1
            else:
                my_dict[s.lower()] = 1

    for k in str2:
        if k == " ":
            continue
        if my_dict.get(k.lower(), False):
            my_dict[k.lower()] -= 1
        else:
            return False

    for _, v in my_dict.items():
        if v != 0:
            return False

    return True

print(is_anagram('Clint Eastwood', 'old we action'))