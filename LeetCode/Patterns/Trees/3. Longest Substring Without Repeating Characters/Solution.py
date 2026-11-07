class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a=""
        maxx=0
        left=0
        for i in range(len(s)):
            while s[i] in a:
                a=a[1:]
                left+=1
            a+=s[i]
            maxx=max(maxx,i-left+1)
        return maxx