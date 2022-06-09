class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        D = {}
        for i in s:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
                
        k = D[s[0]]
        for value in D.values():
            if (value != k):
                return False
        return True