class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxSize = 0
        if not nums:
            return maxSize
        sumIndex = {}
        tmp = 0
        for i in range(len(nums)):
            curSum = tmp + nums[i]
            if curSum == k:
                maxSize = i + 1
            if curSum-k in sumIndex:
                maxSize = max(maxSize,i-sumIndex[curSum-k])
            if curSum not in sumIndex:
                sumIndex[curSum] = i
            tmp = curSum
        return maxSize