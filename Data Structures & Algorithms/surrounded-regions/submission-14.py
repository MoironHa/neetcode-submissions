class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                r, c = stack.pop()

                if (r, c) in visited or board[r][c] == 'X':
                    continue  
                visited.add((r, c))
                capture.add((r, c))
                if r + 1 < ROWS:
                    stack.append((r + 1, c))
                if r - 1 >= 0:
                    stack.append((r - 1, c))
                if c + 1 < COLS:
                    stack.append((r, c + 1))
                if c - 1 >= 0:
                    stack.append((r, c - 1))

            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    capture = set()
                    touches_border = False
                    dfs(i, j)
                    for r, c in capture:
                        if r == 0 or c == 0 or r == ROWS - 1 or c == COLS -1:
                            touches_border = True
                    if not touches_border:
                        for r, c in capture:
                            board[r][c] = 'X'
        return
            