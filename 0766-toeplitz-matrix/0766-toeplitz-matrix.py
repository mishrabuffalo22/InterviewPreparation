class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+1<len(mat) and j+1<len(mat[0]):
                    if mat[i][j] != mat[i+1][j+1]:
                        return 0
        return 1
        