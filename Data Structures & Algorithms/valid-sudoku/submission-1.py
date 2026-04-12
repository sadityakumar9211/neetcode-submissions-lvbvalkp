class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()
        # Check rows
        for i in range(9):
            hashset.clear()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in hashset:
                    return False
                hashset.add(board[i][j])

        # Check columns

        for j in range(9):
            hashset.clear()
            for i in range(9):
                if board[i][j] != "." and board[i][j] in hashset:
                    return False
                hashset.add(board[i][j])

        # Check each 3 by 3 cell
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                hashset.clear()
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] != "." and board[row+i][col+j] in hashset:
                            return False
                        hashset.add(board[row+i][col+j])
        
        return True


