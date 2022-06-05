class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        last = len(x) - 1
        for i in range(len(x)//2):
            if(x[i] != x[last]):
                return False
            last -= 1
        return True