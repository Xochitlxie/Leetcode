class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n%4==0: n/=4
        if n%8==7: return 4
        for i in xrange(0,n+1):
            temp=i*i
            if temp<=n:
                if int((n-temp)**(0.5))**2+temp==n: 
                return 1+ (0 if temp==0 else 1)
            else:
                break 
        return 3