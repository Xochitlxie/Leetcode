import collections
import heapq
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return str
        count = {}
        for char in str:
            count[char] = count.get(char,0) + 1
        l = []
        for c in count:
            l.append((count[c],c))
        heapq.heapify(l)
        queue = collections.deque()
        while len(queue) < k:
            while l:
                queue.append(heapq.heappop(l))
        if len(queue) < k:
            return ""
        print queue
        result = []
        while queue:
            a = queue.popleft()
            print a
            result.append(a[1])
            print result
            if a[0] - 1 > 0:
                heapq.heappush(l,(a[0]-1,a[1]))
            while l:
                queue.append(heapq.heappop(l))
        return "".join(result)