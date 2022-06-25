class Solution:
    def dividing(self, num):
        n = num
        while(num):
            digit = num % 10
            if(digit == 0 or n%digit != 0):
                return False
            num //= 10
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right+1):
            if(self.dividing(i)):
                output.append(i)
        return output