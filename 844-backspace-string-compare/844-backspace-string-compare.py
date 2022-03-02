class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        start1 = len(s)-1
        start2 = len(t)-1
        skip1 = skip2 = 0
        sen1 = sen2 = 0
        while(start1 != -1 or start2 != -1): #check
            if( (start1 != -1 and start2 != -1)and (s[start1] == "#" and t[start2] == "#")):
                skip1 += 1
                skip2 += 1
                start1 -= 1
                start2 -= 1
                continue
            if(start1 != -1):
                if(s[start1] == "#"):
                    skip1 += 1
                    start1 -= 1
                elif(start1 != -1 and skip1 != 0):
                    start1 -= 1
                    skip1 -= 1
                elif(start2 != -1):
                    sen1 = 1
                else:
                    return False
                    start1 = -1
            if(start2 != -1):
                if(t[start2] == "#"):
                    skip2 += 1
                    start2 -= 1
                elif(start2 != -1 and skip2 != 0):
                    start2 -= 1
                    skip2 -= 1
                elif(start1 != -1):
                    sen2 = 1
                else:
                    return False
                    start2 = -1
            if(sen1 == 1 and sen2 == 1):
                if(s[start1] == t[start2]):
                    start1 -= 1
                    start2 -= 1
                    sen1 = 0
                    sen2 = 0
                else:
                    return False
            else:
                sen1 = 0
                sen2 = 0
        if((start1) == (start2)):
            return True
        return False