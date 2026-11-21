class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        count=0
        a=str(num)
        for i in range(len(a)-k+1):
            b=int(a[i:k+i])
            if b!=0 and num%b==0:
                count+=1
        return count
