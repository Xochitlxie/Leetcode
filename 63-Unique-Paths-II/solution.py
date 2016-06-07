class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[1 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
        for i in range(1,len(dp[0])):
            if dp[0][i] != 0:
                dp[0][i] = dp[0][i-1]
        for j in range(1,len(dp)):
            if dp[j][0] != 0:
                dp[j][0] = dp[j-1][0]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if dp[i][j] != 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]