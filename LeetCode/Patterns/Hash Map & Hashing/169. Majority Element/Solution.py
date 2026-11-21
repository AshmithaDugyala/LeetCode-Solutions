class Solution:
    def majorityElement(self, nums):
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        b=max(a,key=a.get)
        return b
