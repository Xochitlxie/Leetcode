class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i]):
                res[j] = tri[i][j] + min(res[j+1],res[j]）
        return res[0]
            