class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        currRow = 0
        down = 1
        length = len(s)
        matrix = [[] for x in range(numRows)]
        for index in range(length):
            matrix[currRow].append(s[index])
            if currRow == 0:
                down = 1
                currRow = 1
            elif currRow == numRows - 1:
                down = 0
                currRow -= 1
            elif down == 1:
                currRow += 1
            else:
                currRow -= 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result = result + matrix[i][j]
        return result