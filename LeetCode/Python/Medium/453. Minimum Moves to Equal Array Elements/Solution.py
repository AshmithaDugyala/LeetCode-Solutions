class Solution(object):
    def minMoves(self, nums):
        
        a=min(nums)
        count=0
        for i in range(len(nums)):
            count+=nums[i]-a
        return count
