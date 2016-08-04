class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        n = len(grid)
        if not n:
            return count
        m = len(grid[0])
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == "1":
                    self.dfsMarker(grid,i,j)
                    count += 1
        return count
                
    def dfsMarker(self,grid,i,j):
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        self.dfsMarker(grid,i+1,j)
        self.dfsMarker(grid,i-1,j)
        self.dfsMarker(grid,i,j+1)
        self.dfsMarker(grid,i,j-1)