class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        tot = 0
        while(n):
            rem = n % 10
            n = n // 10
            prod *= rem
            tot += rem
        return (prod-tot)