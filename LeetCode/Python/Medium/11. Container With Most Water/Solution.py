class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        h=len(height)-1
        area=0
        while(l<=h):
            width=h-l
            a=width*min(height[l],height[h])
            area=max(area,a)
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return area