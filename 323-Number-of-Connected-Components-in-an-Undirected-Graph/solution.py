class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        p = range(n)
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
    
        for e in edges:
            v, w = map(find, e)
            p[v] = w
            n -= v != w
        return n