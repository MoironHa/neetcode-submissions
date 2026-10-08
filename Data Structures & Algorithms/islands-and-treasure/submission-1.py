class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    new_row = r + dr
                    new_col = c + dc
                    if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS or (new_row, new_col) in visited or grid[new_row][new_col] == -1:
                        continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    grid[new_row][new_col] = length 
            length += 1    