class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pacifics = set()
        atlantics = set()

        def pacific(i, j):
            # print(f"pacific called for: {heights[i][j]} with: {i}, {j}")
            visited.add((i, j))
            if i <= 0 or j <= 0 or (i, j) in pacifics:
                # print(f"pacific success with: i <= 0 {i <= 0}, j <= 0 : {j <= 0}, {(i, j)} in pacifics: {(i, j) in pacifics} bc pacifics: {pacifics} ")
                return True
            for dr, dc in neighbors:
                new_row = i + dr
                new_col = j + dc
                if new_row < 0 or new_col < 0:
                    pacifics.add((i, j))
                    # print(f"pacifics: {pacifics}")
                    return True
                if new_row >= ROWS or new_col >= COLS or heights[new_row][new_col] > heights[i][j] or (new_row, new_col) in visited:
                    continue
                if pacific(new_row, new_col):
                    return True
            return False

            
        def atlantic(i, j):
            # print(f"atlantic called for: {heights[i][j]} with: {i}, {j}")
            visited.add((i, j))
            if i >= ROWS or j >= COLS or (i, j) in atlantics:
                return True
            for dr, dc in neighbors:
                new_row = i + dr
                new_col = j + dc
                if new_row >= ROWS or new_col >= COLS:
                    atlantics.add((i, j))
                    return True
                if new_row < 0 or new_col < 0 or heights[new_row][new_col] > heights[i][j] or (new_row, new_col) in visited:
                    continue
                # print("here")
                if atlantic(new_row, new_col):
                    return True
            return False
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                pac = pacific(i, j)
                visited = set()
                atl = atlantic(i, j)
                if pac and atl:
                    # print(f"true for: {i}{j}")
                    res.append((i, j))
        return res

