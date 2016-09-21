class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int 
        """
        maxSize = 0
        dp = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i+1][j+1] = 0
                else:
                    if dp[i][j] > 0 and dp[i+1][j] > 0 and dp[i][j+1]>0:
                        dp[i+1][j+1] = dp[i][j] + 1
                    else:
                        dp[i+1][j+1] = 1
                maxSize = max(maxSize,dp[i+1][j+1])
        return maxSize*maxSize