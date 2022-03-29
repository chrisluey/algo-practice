class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:       
        def tryThing(row: int, col: int, board: List[List[str]], word: str, curr: int, found: List[int]) -> None:
            if len(found) > 0 or row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == "*":
                return
            if board[row][col] == word[curr]:
                if curr >= len(word) - 1:
                    found.append(0)
                    return
                else:
                    temp = board[row][col]
                    board[row][col] = "*"
                    tryThing(row - 1, col, board, word, curr + 1, found)
                    tryThing(row + 1, col, board, word, curr + 1, found)
                    tryThing(row, col - 1, board, word, curr + 1, found)
                    tryThing(row, col + 1, board, word, curr + 1, found)
                    board[row][col] = temp
        temp = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                tryThing(i, j, board, word, 0, temp)
                if len(temp) > 0:
                    return True
        return False
                    
                    