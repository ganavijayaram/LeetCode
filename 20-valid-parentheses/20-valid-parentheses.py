class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if(len(s) % 2 != 0):
            return False
        for i in s:
            if(i == '(' or i=='[' or i=='{'):
                stack.append(i)
            elif(len(stack) != 0):
                closing = stack.pop()
                if(i == ')' and closing != '('):
                    return False
                elif(i == ']' and closing != '['):
                    return False
                elif(i == '}' and closing != '{'):
                    return False
            else:
                return False
        if(len(stack) != 0):
            return False
        return True
                