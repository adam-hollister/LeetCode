from collections import deque

"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
"""
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque() #make a queue of size 'size'
        self.size_queue = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        size = len(self.queue)
        if size > self.size_queue:
            self.queue.popleft()
            size -= 1
        s = sum(self.queue)
        t = s / size
        return round(t, 5)
if __name__ ==  "__main__":
    sol = MovingAverage(3)
    assert sol.next(1) == 1.0, "Test Case 1 Failed"
    assert sol.next(10) == 5.5, "Test Case 2 Failed"
    assert sol.next(3) == 4.66667, "Test Case 3 Failed"
    assert sol.next(5) == 6.0, "Test Case 4 Failed"
    print("All test cases passed!")