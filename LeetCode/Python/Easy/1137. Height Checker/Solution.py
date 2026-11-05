class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
    
        count=0
        b=sorted(heights)
        for i in range(len(b)):
            if heights[i]!=b[i]:
                count+=1
        return count