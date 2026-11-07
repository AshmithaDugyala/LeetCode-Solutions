class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=[]
        c=0
        for i in range(len(digits)):
            if digits[i]!=digits[len(digits)-1]:
                a.append(digits[i])
            elif digits[i]==9:
                c+=1
                a.append(1)
                a.append(0)
                if  c>1:
                    a.remove(a[len(a)])
            else:
                a.append(digits[i]+1)
        return a