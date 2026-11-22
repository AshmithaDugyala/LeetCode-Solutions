class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        a=[]
        for i in range(len(temp)):
            b=0
            for j in range(i+1,len(temp)):
                if temp[i]<temp[j]:
                    b=j-i
                    break
        
            a.append(b)
    
        return a