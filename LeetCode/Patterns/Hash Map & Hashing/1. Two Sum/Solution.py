class Solution(object):
    def twoSum(self, nums, target):
        a={}
        for i,num in enumerate(nums):
            b=target-num
            if b in a:
                return [a[b],i]
            a[num]=i