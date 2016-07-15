# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo,hi = 1,n
        while lo < hi:
            mid = lo + (hi-lo)/2
            print mid,guess(mid)
            lo,hi = ((mid,mid),(mid+1,hi),(lo,mid-1))[guess(mid)]
        return lo