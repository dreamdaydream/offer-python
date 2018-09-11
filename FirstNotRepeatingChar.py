class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s)==0:
            return -1
        value = []
        count = []
        for i in range(len(s)):
            if s[i] not in value:
                value.append(s[i])
                count.append(1)
            else:
                ind = value.index(s[i])
                count[ind] += 1
        for i in range(len(count)):
            if count[i] == 1:
                return s.find(value[i])
                
            
