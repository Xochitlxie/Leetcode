class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums,[],result)
        return result
        
        
    def dfs(self,nums,path,result):
        if not nums:
            if path not in result:
                result.append(path)
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],result)