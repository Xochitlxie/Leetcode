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
        if len(str) == 1:
            return str
        count = {}
        for char in str:
            count[char] = count.get(char,0) + 1
        if len(count) < k:
            return ""
        l = []
        for c in count:
            l.append((-count[c],c))
        heapq.heapify(l)
        queue = collections.deque()
        result = []
        """
        while len(result) < len(str):
            if not l: return ""
            freq,char = heapq.heappop(l)
            queue = collections.deque()
            result.append(char)
            for j in range(k-1):
                if len(result) == len(str): return "".join(result)
                if not l: return ""
                fre,nex = heapq.heappop(l)
                result.append(nex)
                if fre < -1:
                    queue.append((fre+1,nex))
            while queue:
                heapq.heappush(l,queue.pop())
            heapq.heappush(l,(freq+1,char))
        return "".join(result)
        
        """
        while len(queue) < k and l:
            queue.append(heapq.heappop(l))
        #print queue
        while queue:
            if not l and len(queue) < k and queue[0][0] < -1:
                return ""
            a = queue.popleft()
            #print a
            result.append(a[1])
            #print result
            if a[0] + 1 < 0:
                heapq.heappush(l,(a[0]+1,a[1]))
            while l:
                queue.append(heapq.heappop(l))
        return "".join(result)