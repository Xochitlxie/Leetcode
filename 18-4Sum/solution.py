class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Use DFS to record results
        if not candidates or not target: return []
        self.res = []
        path = []
        self.DFS(sorted(candidates), path, target)
        return self.res
        
    def DFS(self, candidates, path, target):
        if target < 0 : return
        elif target == 0:
            self.res.append(path)
        else:
            for i,x in enumerate(candidates):
                if x <= target: # smart search
                    self.DFS(candidates[i:], path +[x], target-x) # this guarantee path node is appended in increasing order
            return
