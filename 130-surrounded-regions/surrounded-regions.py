class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Capture unsurrounded regions (O => Y)
        # Capture surrounded regions (O => X)
        # Uncapture unsurrounded regions (Y => O)
        rows, cols = len(board), len(board[0])
        def markUns(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return
            board[r][c] = 'Y'
            markUns(r + 1, c)
            markUns(r - 1, c)
            markUns(r, c + 1)
            markUns(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    markUns(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'Y':
                    board[r][c] = 'O'
            