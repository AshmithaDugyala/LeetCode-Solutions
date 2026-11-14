class Solution(object):
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
            return 0
        grid[i][j]=0
        count=1
        count+=self.dfs(grid,i+1,j)
        count+=self.dfs(grid,i-1,j)
        count+=self.dfs(grid,i,j+1)
        count+=self.dfs(grid,i,j-1)
        return count
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxx=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=self.dfs(grid,i,j)
                    maxx=max(maxx,area)
        return maxx
            