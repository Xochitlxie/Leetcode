class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r*r == x