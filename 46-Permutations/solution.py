class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums,[],result)
        return result
        
    def dfs(self,nums,path,result):
        if not nums:
            result.append(path)
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],result)