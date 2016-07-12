class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left = 1
        right = x
        while left < right:
            mid = left + (right-left)/2
            if mid <= x/mid:
                left = mid + 1
            else:
                right = mid
        return left - 1