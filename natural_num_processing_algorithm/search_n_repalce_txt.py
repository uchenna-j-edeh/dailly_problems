import os
from os.path import join
import re
def replace_str(filename, old_str, new_str):
    replace = False
    buffer = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:            
            if re.search(old_str, line):
                line = line.replace(old_str, new_str)
                print("Will be replacing", old_str, " with ", new_str, " in file ", filename)
                replace = True
            buffer.append(line)

    if replace:
        f = open(filename, 'w')
        for buf in buffer:                
            f.write(buf)
        f.close()
                                
    
def search_n_replace(path, old_str, new_str):
    for root, _, files in os.walk(path):
        for name in files:
            #print(join(root, name))
            replace_str(join(root, name), old_str, new_str)

search_n_replace('/Users/uchenna/tests', 'you', 'Jehovah')
