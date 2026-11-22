class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j=len(s)-1
        for i in range(len(s)//2):
            s[i],s[j]=s[j],s[i]
            j-=1