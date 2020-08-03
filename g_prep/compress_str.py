"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def solution(my_str):
    new_str = ''
    len_str = len(my_str)
    counter = 1
    for i in range(len_str):
        if len_str - 1 == i:
            if counter >= 1:
                return new_str + repr(counter) + my_str[i]
            return new_str
        if my_str[i+1] == my_str[i]:
            counter = counter + 1
        else:
            new_str = new_str + repr(counter) + my_str[i] 
            counter = 1


print("The solution is: ", solution("aabcccccaaa"))
print("The solution is: ", solution("aabccccca"))

            
