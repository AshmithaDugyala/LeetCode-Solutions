class Solution(object):
    def minMoves(self, nums):
        
        a=max(nums)
        count=0
        for i in range(len(nums)):
            count+=a-nums[i]
        return count
