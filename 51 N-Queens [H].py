# Backtracking, Array

test = 9
def solveNQueens(n):
    boards = []
    col = 0
    board = [["."] * n for x in range(n)]

    def safe(board, row, col):
        # check the row
        if "Q" in board[row]:
            return False
        r = row
        c = col
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        r = row
        c = col
        while r < len(board) and c < len(board):
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        return True

    def solve(board, col):
        # base case
        if col >= n:
            res = []
            for r in board:
                res.append("".join(r))
            boards.append(res)
            return

        # otherwise we loop through all possibilities
        for row in range(len(board)):
            if safe(board, row, col):
                board[row][col] = "Q"
                solve(board, col + 1)
                board[row][col] = "."

    solve(board, col)
    return boards

print(solveNQueens(test))
