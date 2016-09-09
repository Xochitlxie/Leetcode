class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.count(n)

    
    def count(self,n):
        if n == 1:
            return 1
        result = 0
        for i in range(1,n+1):
            left = self.count(i-0)
            right = self.count(n-1-i)
            result += left*right
        return result 