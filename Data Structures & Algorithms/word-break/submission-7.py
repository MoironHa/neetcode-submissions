class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        def dfs(j):
            if len(s) == j:
                return True
            
            curr = root
            for i in range(j, len(s)):
                letter = s[i]
                if letter in curr.children:
                    curr = curr.children[letter]
                    if curr.word:
                        if i not in cache:
                            cache[i] = dfs(i+1)
                        if cache[i]:
                            return True
                else:
                    break
            return False
        cache = {}
        return dfs(0)
            