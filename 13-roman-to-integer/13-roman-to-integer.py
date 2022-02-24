class Solution:
    def romanToInt(self, s: str) -> int:
        tot = 0
        i = 0
        while(i < len(s)):
            if(s[i] == "I"):
                if(i != len(s) - 1):
                    if(s[i+1] == "V"):
                        tot += 4
                        i += 1
                    elif(s[i+1] == "X"):
                        tot += 9
                        i += 1
                    else:
                        tot += 1
                else:
                    tot += 1
            elif(s[i] == "X"):
                if(i != len(s) - 1):
                    if(s[i+1] == "L"):
                        tot += 40
                        i += 1
                    elif(s[i+1] == "C"):
                        tot += 90
                        i += 1
                    else:
                        tot += 10
                else:
                    tot += 10
            elif(s[i] == "C"):
                if(i != len(s) - 1):
                    if(s[i+1] == "D"):
                        tot += 400
                        i += 1
                    elif(s[i+1] == "M"):
                        tot += 900
                        i += 1
                    else:
                        tot += 100
                else:
                    tot += 100
            elif(s[i] == "V"):
                tot += 5
            elif(s[i] == "L"):
                tot += 50
            elif(s[i] == "D"):
                tot += 500
            elif(s[i] == "M"):
                tot += 1000
            i += 1
        return tot