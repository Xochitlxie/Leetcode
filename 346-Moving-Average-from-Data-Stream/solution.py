import collections
        
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        self.sum = 0
        self.size = size


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if not self.queue:
            self.queue.append(val)
            return float(val)
        else:
            self.sum = self.sum - self.queue.popleft() + val
            self.queue.append(val)
            return float(self.sum))/self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)