"""
Assuming you need to keep a running average of what some function returns. And further,
you need to do this for a family of functions or methods. We can write a decorator called
running_average to handle this - as you read, note carefully how data is defined and
used:
"""

def running_average(func):
    """
    Each time the function is called, the average of all calls so far is printed out. Decorator
    functions are called once for each function they are applied to. Then, each time that function
    is called in the code, the wrapper function is what’s actually executed
    This creates internal dictionary, name data, that is used to keep track of foo's mstrics
    """
    data = {"total" : 0, "count" : 0}
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print("Average of {} so far: {:.01f}".format(func.__name__, data["total"] / data["count"]))
        return func(*args, **kwargs)
    return wrapper

@running_average
def foo(x):
    return x + 2

@running_average
def bar(x, y):
    return x * y

if __name__ == "__main__":
    for x in range(10):
        foo(x)
        bar(x, x+1)
  
