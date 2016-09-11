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
            diff.append(nums[i] - nums[i-1])
        if len(nums) <= 1:
            if nums[0] < 0:
                return 3
        prod = []
        for j in range(1,len(diff)):
            prud.append(prod[i]*prod[i-1])
        maxLen = 0
        count = 0
        for num in prod:
            if num < 0:
                count += 1
                maxLen = max(count,maxLen)
            else:
                count = 0
        return maxLen+2