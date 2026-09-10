# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val
        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if right < 0: right = 0
            if left < 0: left = 0
            maxPath = max(maxPath, left + right + node.val)
            return node.val + max(left , right)
        dfs(root)
        return maxPath
        
