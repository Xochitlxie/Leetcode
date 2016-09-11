class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = []
        if len(nums) <= 1:
            return len(nums)
        for i in range(1,len(nums)):
            diff[i-1] = nums[i] - nums[i-1]
        maxLen = 0
        count = 0
        for num in diff:
            if num > 0:
                count += 1
                maxLen = max(count,maxLen)
            else:
                count = 0
        return maxLen
        
        