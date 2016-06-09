class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        
        pre = costs[0][:]
        now = [0]*3
        
        for i in range(n-1):
            now[0] = min(pre[1],pre[2]) + costs[i+1][0]
            now[1] = min(pre[0],pre[2]) + costs[i+1][1]
            now[2] = min(pre[0],pre[1]) + costs[i+1][2]
            pre[:] = now[:]
        
        return min(pre)