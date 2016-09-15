class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        F0 = 0
        total = sum(A)
        for i in range(len(A)):
            F0 += i * A[i]
        for j in range(1,len(A)):
            next = dp-sum+len(A)*A[i-1]
            dp = max(dp,next)
        return dp