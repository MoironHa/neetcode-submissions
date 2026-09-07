class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()

        def helper(i):
            if i >= n:
                solution.append([''.join(row) for row in board])
            for j in range(n):
                if j in cols or (i-j) in posDiag or (i+j) in negDiag:
                    continue
                board[i][j] = 'Q'
                cols.add(j)
                posDiag.add(i-j)
                negDiag.add(i+j)

                helper(i + 1)
                cols.remove(j)
                posDiag.remove(i-j)
                negDiag.remove(i+j)
                board[i][j] = '.'
        helper(0)
        return solution