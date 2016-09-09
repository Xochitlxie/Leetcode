class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.count(n)

    
    def count(self,n):
        if n == 0:
            return 1
        result = 0
        for i in range(1,n+1):
            left = self.count(i-1)
            right = self.count(n-i)
            result += left*right
        return result 