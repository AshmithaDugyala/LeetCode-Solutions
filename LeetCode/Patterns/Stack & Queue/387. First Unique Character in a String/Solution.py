class Solution(object): 
    def firstUniqChar(self, s): 
        count = {} 
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]]=1
            else:
                count[s[i]]+=1 
 
        for i in range(len(s)): 
            if count[s[i]] == 1: 
                return i 
 
        return -1