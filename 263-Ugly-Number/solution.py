class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        uglyFactor = (2,3,5)
        for i in uglyFactor:
            while num%i == 0:
                num = num/i
        return num == 1    
        