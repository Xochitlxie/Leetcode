class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        end = [None] * len(envelopes)
        hi = 0
        for _, h in sorted(envelopes, key=lambda (w, h): (w, -h)):
            i = bisect.bisect_left(end, h, hi=hi)
            end[i] = h
            hi += i == hi
        return hi