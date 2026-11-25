class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=set(nums)
        a=[]
        for i in range(1,len(nums)+1):
            if i not in b:
                a.append(i)
        return a
                
