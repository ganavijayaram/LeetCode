class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        length =  len(words)
        length -= 1
        D = {}
        #str_length = len(order)
        for i in range(26):
            D[order[i]] = i 
        for i in range(length):
            if(len(words[i]) < len(words[i+1])):
                word_length = len(words[i])
            else:
                word_length = len(words[i+1])
            for j in range(word_length):
                if(D[words[i][j]] >  D[words[i+1][j]]):
                    return False
                elif(D[words[i][j]] <  D[words[i+1][j]]):
                    break
            else:
                if(len(words[i]) > len(words[i+1])):
                    return False
        return True
            