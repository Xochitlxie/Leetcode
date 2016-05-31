class Solution(object):
    result = []
    def combinationSum2(self, candidates, target):
        self.result = []
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
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                self.dfs(candidates,i+1,path+[candidates[i]],target-candidates[i])