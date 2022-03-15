class Solution:
    def isHappy(self, n: int) -> bool:
        D = {}
        while(n != 1):
            if(n in D):
                return False
            D[n] = 1
            s = str(n)
            tot = 0
            for i in s:
                i = int(i)
                tot += i**2
            n = tot
        return True