class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        nums.sort()
        while(i<len(nums)-1):
            if nums[i]+nums[i+1]==target:
                return 2
            if nums[i]==target or nums[i+1]==target:
                return 1
            i+=1
        return 0
                