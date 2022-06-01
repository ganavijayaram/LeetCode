class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        D = {}
        for i in magazine:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        for i in ransomNote:
            if i in D:
                D[i] -= 1
                if(D[i] == 0):
                    del D[i]
            else:
                return False
        return True