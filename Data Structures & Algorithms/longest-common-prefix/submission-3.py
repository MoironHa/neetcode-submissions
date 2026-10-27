class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode("")
        for word in strs:
            if word == "":
                return word
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode(char)
                curr = curr.children[char]
            curr.word = True

        def explore(node):
            nonlocal res
            if len(node.children) == 1:
                child = next(iter(node.children.values()))
                res = res + child.val
                if child.word:
                    return
                explore(child)
        res = ""
        explore(root)
        return res