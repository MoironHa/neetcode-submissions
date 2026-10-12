class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        shortest = {}
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while heap:
            w1, r1, c1 = heapq.heappop(heap)
            n1 = grid[r1][c1]
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for dr, dc in neighbors:
                new_row = r1 + dr
                new_col = c1 + dc
                if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS or grid[new_row][new_col] in shortest:
                    continue
                heapq.heappush(heap, (max(grid[new_row][new_col], w1), new_row, new_col))
        return shortest[grid[ROWS - 1][COLS - 1]]