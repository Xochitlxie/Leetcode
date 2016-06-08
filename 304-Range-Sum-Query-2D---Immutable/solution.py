class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if (not matrix) or (not matrix[0]):
            self.sum = []
        else:
            m = len(matrix)
            n = len(matrix[0])
            dp = [[0 for i in range(n)] for j in range(m)]
            dp[0][0] = matrix[0][0]
            for i in range(1,n):
                dp[0][i] = dp[0][i-1] + matrix[0][i]
            for i in range(1,m):
                dp[i][0] = dp[i-1][0] + matrix[i][0]
            for i in range(1,m):
                for j in range(1,n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            self.sum = dp
        print self.dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if len(self.sum) == 0:
            return 0
        if row1 == 0 and col1 == 0:
            return self.sum[row2][col2]
        elif row1 == 0:
            return self.sum[row2][col2] - self.sum[row2][col1-1]
        elif col1 == 0:
            return self.sum[row2][col2] - self.sum[row1-1][col2]
        else:
            return self.sum[row2][col2] - self.sum[row1-1][col2] - self.sum[row2][col1-1] + self.sum[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)