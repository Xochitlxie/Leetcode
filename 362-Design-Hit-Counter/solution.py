from collection import deque
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = deque()
        self.map = {}
        self.count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.count or self.times[-1] != timestamp:
            self.times.append(timestamp)
            self.map[timestamp] = 1
        else:
            self.map[timestamp] += 1
        self.count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.count and self.times[0] <= timestamp - 300:
            self.count -= self.map[self.time[0]]
            self.times.popleft()
        return self.count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)