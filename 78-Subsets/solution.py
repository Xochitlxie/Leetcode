class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not nums:
            return result
        nums.sort()
        for i in range(1,len(nums)+1):
            self.dfs(i,nums,[],result)
        return result
        
    def dfs(self,capacity,nums,subset,result):
        if capacity == 0:
            result.append(subset)
            return
        for i in range(len(nums)):
            self.dfs(capacity-1,nums[i:],subset+[nums[i]],result)