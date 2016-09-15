class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        dp = 0
        result = -sys.maxint
        total = sum(A)
        for i in range(len(A)):
            dp += i * A[i]
        for j in range(1,len(A)):
            dp = dp-total+len(A)*A[j-1]
            result = math.max(dp,result)
        return max