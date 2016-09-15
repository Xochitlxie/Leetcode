class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        dp = 0
        total = sum(A)
        print total
        for i in range(len(A)):
            dp += i * A[i]
        result = dp
        for j in range(1,len(A)):
            next = dp-total+len(A)*A[j-1]
            result = max(next,result)
            dp = next
        return result