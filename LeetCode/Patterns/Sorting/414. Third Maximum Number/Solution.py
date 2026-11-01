class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=list(set(nums))
        b.sort(reverse=True)
        if len(b)>=3:
            return b[2]
        else:
            return b[0]