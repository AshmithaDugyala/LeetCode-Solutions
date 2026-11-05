class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1 and nums[0]>0:
            return True
        current=0
        jumps=0
        maxx=0
        for i in range(len(nums)-1):
            maxx=max(maxx,i+nums[i])

            if i==current:
                jumps+=1
                current=maxx
        return maxx==nums[len(nums)-1]
