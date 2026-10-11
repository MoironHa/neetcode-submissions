class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
             

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isDiff(word1, word2):
            diffs = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diffs += 1
            return diffs == 1
        visited = set()
        root = Node(beginWord)
        visited.add(root.val)
        curr = root
        count = 1
        res = 0
        
        def build(node):
            queue = deque()
            queue.append(node)
            while queue:
                curr = queue.popleft()
                for word in wordList:
                    if word in visited:
                        continue
                    if isDiff(curr.val, word):
                        curr.children.append(Node(word))
                        visited.add(word)
                for child in curr.children:
                    queue.append(child)
        build(root)
        for child in root.children:
            build(child)
        def dfs(node):
            nonlocal count, res
            if node.val == endWord:
                res = count
            count += 1
            for child in node.children:
                dfs(child)
            count -= 1

            return count
        dfs(root)
        return res