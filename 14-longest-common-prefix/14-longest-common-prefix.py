class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1):
            return strs[0]
        elif(len(strs) == 0):
            return ""
        else:
            common_prefix = len(strs[0])
            for i in range(len(strs)-1):
                if(len(strs[i+1]) < common_prefix):
                    common_prefix = len(strs[i+1])
                j=0
                while(j < common_prefix):
                    if(strs[i][j] != strs[i+1][j]):
                        break
                    j += 1
                else:
                    j += 1
                if(j < common_prefix):
                    common_prefix = j
            return(strs[0][:common_prefix])
                    