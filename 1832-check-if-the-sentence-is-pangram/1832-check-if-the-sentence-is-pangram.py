class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        D = {}
        for i in sentence:
            D[i] = 1
        if(len(D.keys()) == 26):
            return True
        return False