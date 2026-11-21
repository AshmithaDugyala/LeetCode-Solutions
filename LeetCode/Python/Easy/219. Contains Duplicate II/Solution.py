class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        j=1
        for i in range(len(nums)):
            if nums[i]!=nums[j] and abs(i-j)<=k:
                j+=1
        