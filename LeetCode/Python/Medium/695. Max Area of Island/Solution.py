class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxx=0
        for i in grid:
            maxx=max(maxx,sum(i))
        return maxx