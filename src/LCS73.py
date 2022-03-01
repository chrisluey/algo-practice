class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        this_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        this_set.add((k,j))
                    for l in range(len(matrix[0])):
                        this_set.add((i,l))
        
        for ele in this_set:
            matrix[ele[0]][ele[1]] = 0
        