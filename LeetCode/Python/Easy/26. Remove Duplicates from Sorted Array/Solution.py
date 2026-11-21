class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
        for i in range(len(a)):
            nums[i]=a[i]
        return len(a)