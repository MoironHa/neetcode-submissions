class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacifics = set()
        atlantics = set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or prevHeight > heights[r][c]:
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for i in range(COLS):
            dfs(0, i, pacifics, heights[0][i])
            dfs(ROWS - 1, i, atlantics, heights[ROWS - 1][i])
        for i in range(ROWS):
            dfs(i, 0, pacifics, heights[i][0])
            dfs(i, COLS - 1, atlantics, heights[i][COLS - 1])

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pacifics and (i, j) in atlantics:
                    res.append((i, j))
        return res
        