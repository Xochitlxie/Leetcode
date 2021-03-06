class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(k,res):
            if k <= n:
                res.append(k)
            t = k*10
            if t <= n:
                for i in range(10):
                    dfs(t+i,res)
        res = []
        for i in range(1,10):
            dfs(i,res)
        return res
