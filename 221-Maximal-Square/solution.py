class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int 
        """
        if (not matrix) or (not matrix[0]):
            return 0
        n = len(matrix)
        m = len(matrix[0])
        table = [[0]*(m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] == 1 or matrix[i-1][j-1] == "1":
                    table[i][j] = min(table[i-1][j-1],table[i-1][j],table[i][j-1]) + 1
                else:
                    table[i][j] = 0
        max_continous = 0
        for i in xrange(len(table)):
            for j in xrange(len(table[0])):
                max_continous = max(max_continous,table[i][j])
        result = max_continous * max_continous
        return result