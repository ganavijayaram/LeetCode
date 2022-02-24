class Solution:
    def converttodec(self, binary):
        j = 0
        dec = 0 
        for i in range(len(binary)-1, -1, -1):
            dec += int(binary[i])*(2**j)
            j += 1
        return dec
    def converttobin(self, decimal):
        lst = []
        if(decimal == 0):
            return "0"
        while(decimal):
            rem = decimal % 2
            lst.insert(0, rem)
            decimal //= 2
        str1 = ''.join(str(e) for e in lst)
        return(str1)
    def addBinary(self, a: str, b: str) -> str:
        dec = (self.converttodec(a) +  self.converttodec(b))
        return(self.converttobin(dec))
        