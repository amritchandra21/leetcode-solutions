class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for i in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                res.append(["".join(k) for k in board])
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                posDiag.add(r + c)
                negDiag.add(r - c)
                cols.add(c)
                board[r][c] = "Q"

                backtrack(r + 1)

                posDiag.remove(r + c)
                negDiag.remove(r - c)
                cols.remove(c)
                board[r][c] = "."
        backtrack(0)
        return res

