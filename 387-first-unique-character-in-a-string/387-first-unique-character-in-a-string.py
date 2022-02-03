class Solution:
    def firstUniqChar(self, s: str) -> int:
        if(len(s) ==  1):
            return 0
        for i in range(len(s)):
            for j in range (len(s)):
                if(i!= j and s[i] == s[j]):
                    break
            else:
                return i
        return -1