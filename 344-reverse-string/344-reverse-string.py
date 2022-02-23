class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for  i in range(len(s)):
            letter = s.pop()
            s.insert(i, letter)