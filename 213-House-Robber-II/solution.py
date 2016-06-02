class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.dp(nums[:-1]),self.dp(nums[1:]))
        
    def dp(self,nums):
        rob = nums[0]
        notRob = 0
        for i in range(1,len(nums)):
            rob,notRob = notRob + nums[i], max(rob,notRob)
        return max(rob,notRob)