class Solution:
    def toLowerCase(self, s: str) -> str:
        p = ""
        for i in range(len(s)):
            if(ord(s[i])>=65 and ord(s[i])<=90):
                p += chr(ord(s[i]) + 32)
            else:
                p += s[i]
        return p