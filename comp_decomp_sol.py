# using list as stack
"""
translate '3[abc]4[ab]c' into abcabcabcabababc
"""
import sys

stack  = []    

def decompress(args):
    #stack = []    
    global stack

    for i, elem in enumerate(args):
        if elem == ']':
            process_stack()
        else:
            stack.append(elem)

    print(''.join(stack))

def process_stack():
    global stack

    collection = ""    
    print ('stack: ', stack)

    j = len(stack) # last index
    for i in range(j):

        val = stack.pop()

        if val == '[':
            number = calculate_digits()
            stack.append(collection*int(number))        
            break

        collection = collection + val


def calculate_digits():
    global stack
    j = len(stack)
    total = ""
    for i in range(j):
        val = stack.pop()

        if not val.isdigit():
            stack.append(val)
            return total 

        if not len(stack):
            return val + total

        total = val + total
if __name__ == '__main__':
        decompress(sys.argv[1])
