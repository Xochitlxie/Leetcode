class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num &(num-1) == 0 and num & int("1010101010101010101010101010101",2)== num