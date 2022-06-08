class Solution:
    def digitCount(self, num: str) -> bool:
        D = {}
        num = str(num)
        for i in num:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        for i in range(len(num)):
            if(str(i) not in D):
                if(int(num[i]) != 0):
                    return False
            elif(D[str(i)]) != int(num[i]):
                return False
        return True