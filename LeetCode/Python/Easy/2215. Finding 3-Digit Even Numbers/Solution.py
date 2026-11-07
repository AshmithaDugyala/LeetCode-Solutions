class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j!=k and k!=i:
                        nums=digits[i]*100+digits[j]*10+digits[k]
                        if digits[i]!=0 and digits[k]%2==0:
                            a.append(nums)
        return sorted(set(a))


