class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        D = {}
        for i in s:
            if i not in D:
                D[i] = 1
            else:
                D[i] += 1
        for i in t:
            if i not in D:
                return i
            else:
                D[i] -= 1
                if(D[i] == 0):
                    del D[i]
        