import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.MIN_INT = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(val <  self.MIN_INT):
            self.MIN_INT = val
        

    def pop(self) -> None:
        if(self.MIN_INT ==self.stack.pop()):
            self.MIN_INT = sys.maxsize
            for i in self.stack:
                if(self.MIN_INT > i):
                    self.MIN_INT = i
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.MIN_INT
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()