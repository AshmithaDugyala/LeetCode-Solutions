class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        count=0
        for i in range(len(s)):
            if s[i]=="(" and s[i+1]==")":
                count+=2
                while len(s)==0:
                    s.pop()
            else:
                stack.append(i)
        return count
            
