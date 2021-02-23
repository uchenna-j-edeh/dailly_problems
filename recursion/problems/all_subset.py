# Complete the function below.



def helper(s, i, result, slate):
    #base case
    if i == len(s):
        result.append(slate)
        return
    
    #recursive case
    helper(s, i+1, result, slate) #exclude
    helper(s, i+1, result, slate+s[i]) # include
    
def generate_all_subsets(s):
    result = []
    helper(s, 0, result, "")
    return result

print(generate_all_subsets('abcd'))
