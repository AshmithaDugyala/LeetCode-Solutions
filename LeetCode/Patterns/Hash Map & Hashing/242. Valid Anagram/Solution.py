"""
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1
        for i in count:
            if i != 0:
                return False
                
        return True"""
class Solution(object):
    def isAnagram(self, s, t):
        a=""
        for i in s:
            if i not in t:
                a+="i"
            if len(s)!=len(t):
                return False
            if s.count(i) != t.count(i):
                return False

        return (len(a))==0  
