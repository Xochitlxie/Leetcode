class Solution(object):
    def integerReplacement(self, n,counter = 0):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return counter
    	if not n%2: return self.integerReplacement(n/2, counter+1)
    	else: return min(self.integerReplacement(n+1, counter+1), self.integerReplacement(n-1, counter+1))