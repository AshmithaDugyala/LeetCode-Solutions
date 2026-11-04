"""class Solution(object):
    def productExceptSelf(self, nums):
        b=[]
        a=1
        count=0
        for i in range(len(nums)):
            a*=nums[i]
        
        for i in range(len(nums)):
            if nums[i]:
                b.append(a/nums[i])
        return b
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i != j:
                    p *= nums[j]
            b.append(p)
        return b"""
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]

        return answer
        

