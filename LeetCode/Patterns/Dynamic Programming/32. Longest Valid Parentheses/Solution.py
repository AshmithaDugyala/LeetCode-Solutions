class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    count=max(count,i-stack[-1])
        return count



"""class Solution(object):
    def longestValidParentheses(self, s):
        stack=[]
        count=0
        for i in range(len(s)-1):
            if s[i]=="(" and s[i+1]==")":
                count+=2
                while len(s)==0:
                    s.pop()
            else:
                stack.append(i)
        return count"""
            
