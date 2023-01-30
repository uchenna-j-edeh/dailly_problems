
import time
import os

def large_file(path):
    print(f"I am currently in: {os.getcwd()}")
    count = 0
    start = time.time()
    with open(path) as file_obj:
        for line in file_obj:
            print(line)
            count = count + 1
    emd = time.time()


large_file('wiki_RAID.txt')
