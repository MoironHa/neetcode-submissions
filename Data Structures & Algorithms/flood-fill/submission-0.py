class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = []
        condition = image[sr][sc]
        def dfs(i, j):
            print(f"called with: {i} {j}")
            visited.append((i, j))
            if image[i][j] == condition:
                print("here")
                image[i][j] = color
            else:
                return
            if (i + 1, j) not in visited and i + 1 < len(image):
                dfs(i+1, j)
            if (i, j + 1) not in visited and j + 1 < len(image[0]):
                dfs(i, j+1)
            if (i - 1, j) not in visited and i - 1 >= 0:
                dfs(i-1, j)
            if (i, j - 1) not in visited and j - 1 >= 0:
                dfs(i, j - 1)
        dfs(sr, sc)
        return image