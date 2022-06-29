class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        last = length - 1
        tot = 0
        for i in range(length):
            tot += mat[i][i]
            tot += mat[i][last]
            last -= 1
        if(length%2 != 0):
            tot -= mat[length//2][length//2]
        return tot