class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        index = s.rfind(' ')
        if(index == -1):
            return len(s)
        return (len(s[index+1: len(s)]))