class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        D = {}
        count = 0
        for i in jewels:
            D[i] = 1
        for j in stones:
            if j in D:
                count += 1
        return count
                