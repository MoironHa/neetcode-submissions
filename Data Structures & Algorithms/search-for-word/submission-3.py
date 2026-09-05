class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        ans = False
        def helper(i, j, k, curr):
            nonlocal visited, ans
            curr = curr + board[i][j]
            if len(curr) == len(word):
                if curr == word:
                    ans = True
                return
            visited.append((i, j))
            if i - 1 >= 0 and board[i - 1][j] == word[k+1] and (i-1, j) not in visited:
                helper(i - 1, j, k+1, curr)
            if i + 1 < len(board) and board[i + 1][j] == word[k+1] and (i+1, j) not in visited:
                helper(i + 1, j, k+1, curr)
            if j - 1 >= 0 and board[i][j-1] == word[k+1] and (i, j - 1) not in visited:
                helper(i, j-1, k+1, curr)
            if j + 1 < len(board[0]) and board[i][j + 1] == word[k+1] and (i, j + 1) not in visited:
                helper(i, j+1, k+1, curr)
            visited.remove((i, j))
            
            
            
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0]:
                    helper(i, j, 0, '')
        return ans