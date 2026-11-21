class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """     
        j=0
        b=0
        ans=float('INF')
        for i in range(len(nums)):
            b+=nums[i]

            while (b>=target):
                ans=min(ans,i-j+1)
                b-=nums[j]
                j+=1
        if ans==float('INF'):
            return 0
        return ans



        
        