class Solution(object):
    self.result = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidated.sort()
        self
        
    def dfs(self, candidates, index, path, target):
        if target == 0:
            result.append(path)
            return
        else:
            for i in range(index+1,len(candidates)):
                if candidates[i] > target:
                    break
                else:
                    self.dfs(candidates,index,path.append(candidates[i]),target-candidates[i])