class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        return self.hammingWeight(n & n-1, count+1) if n!=0 else count 