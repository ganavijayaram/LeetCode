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
        #dec = (self.converttodec(a) +  self.converttodec(b))
        #return(self.converttobin(dec))
        lista = list(a)
        listb = list(b)
        if(len(a) < len(b)):
            length = len(b)-len(a)
            for i in range(length):
               lista.insert(0, 0)
        else:
            length = len(a)-len(b)
            for i in range(length):
               listb.insert(0, 0)
        carry = 0
        listc = []
        for i in range(len(lista)-1, -1, -1):
            xor = int(lista[i]) ^ int(listb[i])
            final = xor ^ carry
            if((xor == 0 and int(lista[i]) == 1) or (final == 0 and carry ==  1)):
                carry = 1
            else:
                carry = 0
            listc.insert(0, final)
        if(carry == 1):
            listc.insert(0, carry)
        str1 = ''.join(str(e) for e in listc)
        return str1

        