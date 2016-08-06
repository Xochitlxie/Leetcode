class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        count = 0
        checkSet = set()
        for edge in edges:
            if edge[0] not in checkSet and edge[1] not in checkSet():
                count += 1
            else:
                checkSet.add(edge[0])
                checkSet.add(edge[1])
        for i in xrange(n):
            if i not in checkSet:
                count += 1
        return count