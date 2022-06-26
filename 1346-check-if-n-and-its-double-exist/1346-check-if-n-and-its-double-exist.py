class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        D = {}
        for i in range(len(arr)):
            if(arr[i] in D):
                D[arr[i]] += 1
            else:
                D[arr[i]] = 1
        for i in arr:
            if(i == 0):
                if(D[0] > 1):
                    return True
            elif(i*2 in D):
                return True
        return False