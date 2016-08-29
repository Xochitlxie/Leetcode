class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for c in s:
            res ^= c
        for ch in t:
            res ^= ch
        return res