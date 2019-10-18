"""
Look at a directory. Check for a file n-times. if the file is there anytime during the check
exit. Otherwise create it after check n-times
"""
import os
import click
import functools
import time

# lifted off from the real python and tweaked a bit
TRIES = 10
DELAY = 3 # seconds

def repeat(tries=2, delay=0, sentinel=True):
    """
    sentinel: if you see this value before timeout is over, quit retrying, return value
    """
    
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(tries):
                time.sleep(delay)
                value = func(*args, **kwargs)
                if value is sentinel:
                    break
            return value
        return wrapper_repeat

    return decorator_repeat
    
@repeat(tries=TRIES, delay=DELAY)
def scan_dir(path, filename):
    fname = os.path.join(path, filename)
    print("Looking for file {0} in a folder {1}...".format(filename, path))
    if os.path.exists(path):
        # files_in_dir = os.listdir()
        if os.path.exists(fname):
            print("Found the filename: {}".format(fname))
            return True
        #raise IOError("File {} does not exist yet. Create it first".format(filename))

        

@click.command()
@click.option("--path", default="", help="full path of the folder to be scanned.")
@click.option("--filename", default="", help="The filename to be scanned.")
def main(path, filename):
    if not len(path):
        click.prompt("Provide the file path here: ")
    if not len(filename):
        click.prompt("Enter the name of the file here: ")

    try:
        scan_dir(path, filename)
    except IOError:
        print("File does not exist, create it first.")

if __name__ == '__main__':
    main()
    