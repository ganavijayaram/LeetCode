class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        length = 0
        for i in s:
            if(i == "#"):
                if(length != 0):
                    stack1.pop()
                    length -= 1
            else:
                stack1.append(i)
                length += 1
        stack2 = []
        length = 0
        for i in t:
            if(i == "#"):
                if(length != 0):
                    stack2.pop()
                    length -= 1
            else:
                stack2.append(i)
                length += 1
        return(stack1 == stack2)