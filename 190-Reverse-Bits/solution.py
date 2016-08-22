class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            reversed |= (n >> i) & 0x1
        return reversed