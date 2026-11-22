class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0
        for i in t:
            if j<en(s) and s[j]==i:
                j+=1
        return j==len(s)