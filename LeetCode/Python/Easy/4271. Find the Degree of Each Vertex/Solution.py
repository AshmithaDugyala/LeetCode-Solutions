class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        a=[]
        for i in matrix:
            a.append(sum(i))
        return a
