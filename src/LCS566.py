class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not len(mat) * len(mat[0]) == r * c:
            return mat
        result = [[0 for x in range(c)] for y in range(r)]
        i, j = 0, 0
        for x in range(r):
            for y in range(c):
                result[x][y] = mat[i][j]
                if j + 1 >= len(mat[0]):
                    j = 0
                    i += 1
                else:
                    j += 1     
        return result