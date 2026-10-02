class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
        visited = set()
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        queue.append((0,0))
        visited.add((0,0))
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]



        length = 1          
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for dr, dc in neighbors:
                    new_row = r + dr
                    new_col = c + dc
                    if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS or (new_row, new_col) in visited or grid[new_row][new_col] == 1:
                        continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
            length += 1
        return -1
            
