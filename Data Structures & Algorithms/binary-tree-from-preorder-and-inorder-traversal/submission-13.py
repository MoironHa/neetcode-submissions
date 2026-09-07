# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val : i for i, val in enumerate(inorder)}
        prIdx = 0
        inIdx = 0
        def helper(limit):
            nonlocal prIdx, inIdx
            if prIdx >= len(preorder):
                return
            if inorder[inIdx] == limit:
                inIdx += 1
                return
            node = TreeNode(preorder[prIdx])
            prIdx += 1
            node.left = helper(node.val)
            node.right = helper(limit)
            return node
        
        return helper(float('inf'))