
"""
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.

"""
from queue import Queue

class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.total_so_far = 0
        self.queue = Queue(self.size)

    def next(self, val):
        if self.queue.qsize() == self.size:
            item = self.queue.get()
            self.total_so_far -= item
            
        self.queue.put(val)
        self.total_so_far += val


        return self.total_so_far / self.queue.qsize()



# setup 
#Explanation
movingAverage = MovingAverage(3)
print(movingAverage.next(1)) # return 1.0 = 1 / 1
print(movingAverage.next(10)) # return 5.5 = (1 + 10) / 2
print(movingAverage.next(3)) # return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5)) # return 6.0 = (10 + 3 + 5) / 3


