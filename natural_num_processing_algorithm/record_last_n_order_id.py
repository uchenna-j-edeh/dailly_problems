"""
You run an e-commerce website and want to record the last N order ids in a log
Implement a data structure to accomplish this, with the following API:
* record(order_id): adds the order to the log
* get_last(i): gets the ith last element from the log. i is guranteed to be smaller than or equal to N
You should be as efficient with time and space as possible
"""
import sys

DB_NAME = 'db.txt'

def record(order_id):
    #import pdb; pdb.set_trace()
    with open(DB_NAME, 'a') as fh:
        fh.write(order_id + '\n')  

def get_last(i):
    i = int(i)
    try:
        with open(DB_NAME) as fh:
            lines = fh.readlines()
    except IOError:
        raise IOError('You likely need to add item first...')

    if i > 0 and i <= len(lines): # avoid wrap around
        return lines[i - 1].strip()

    return None

def solution(action, vals):
    if action == 'record':
        record(vals)

    elif action == 'get_last':
        return get_last(vals)

def main(args):
    if len(args) != 3:
        raise AssertionError("Usage:\n\tpython3 {0} {1} {2}\n\t".format(__file__, 'record', 'Item1'))
    print(solution(args[1], args[2]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except (IOError, AssertionError) as e:
        print(e)
        sys.exit(1)

