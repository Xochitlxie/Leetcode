class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums =  [i for i in range(1,n+1)]
        result = []
        self.dfs(k,nums,[],result)
        return result
        
    def dfs(self,capacity,nums,sub,result):
        if capacity == 0:
            result.append(sub)
            return
        for i in range(len(nums)):
            self.dfs(capacity-1,nums[i:],sub+[nums[i]],result)