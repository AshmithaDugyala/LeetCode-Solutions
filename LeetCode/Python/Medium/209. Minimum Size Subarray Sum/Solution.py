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
            b+=nums[i]
            if nums[i]+nums[i+1]==target:
                a=[i,i+1]
                return len(a)
            if nums[i]==target or nums[i+1]==target:
                a=[i]
                return len(a)
            i+=1
        return 0
        
        