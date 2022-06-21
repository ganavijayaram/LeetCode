class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if(carry == 1 and digits[i] == 9):
                digits[i] = 0
                carry = 1
            elif(carry == 0):
                break
            else:
                digits[i] += 1
                carry = 0
        if(carry):
            digits.insert(0, 1)
        return digits