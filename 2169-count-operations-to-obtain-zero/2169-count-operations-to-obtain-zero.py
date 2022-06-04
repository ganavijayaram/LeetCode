class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while(not(num1 == 0 or num2 == 0)):
            if(num1 < num2):
                num2 = num2 - num1
            else:
                num1 = num1 - num2
            count += 1
        return count