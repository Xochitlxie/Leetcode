class Solution(object):
    result = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.dfs(candidates,0,[],target)
        return self.result
        
    def dfs(self, candidates, index, path, target):
        if target == 0:
            self.result.append(path)
            return
        else:
            for i in range(index+1,len(candidates)):
                if candidates[i] > target:
                    break
                else:
                    self.dfs(candidates,index+1,path+[candidates[i]],target-candidates[i])