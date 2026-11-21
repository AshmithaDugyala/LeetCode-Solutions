class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(n):
            count+=1
        return count