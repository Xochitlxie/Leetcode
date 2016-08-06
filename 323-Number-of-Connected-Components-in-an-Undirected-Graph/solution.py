class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        p = range(n)
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]
        for e in edges:
            v, w = map(find, e)
            p[v] = w
            n -= v != w
        return n