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
        return self.guessSearch(1,n)
        
    def guessSearch(self,start,end):
        mid = start + (end-start)/2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            return self.guessSearch(start,mid)
        else:
            return self.guessSearch(mid+1,end)