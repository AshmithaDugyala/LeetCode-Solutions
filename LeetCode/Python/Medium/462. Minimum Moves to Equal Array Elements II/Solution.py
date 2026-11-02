class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums
        a=nums[len(nums)//2]
        count=0
        for i in range(len(nums)):
            count+=abs(a-nums[i])
        return count