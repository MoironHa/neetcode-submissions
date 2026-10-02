class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        mins = -1

    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        if not queue:
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1:
                        return -1
            return 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    new_row = r + dr
                    new_col = c + dc

                    if min(new_row, new_col) < 0 or new_row >= ROWS or new_col >= COLS or grid[new_row][new_col] == 0 or grid[new_row][new_col] == 2:
                        continue
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))
            mins += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mins 