class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        visited = set()
        for word in words:
            for char in word:
                if char not in visited:
                    visited.add(char)
                    adj[char] = set()
        def buildGraph(word1, word2):
            l = 0
            r = 0

            while l < len(word1) and r < len(word2):
                if word1[l] == word2[r]:
                    l += 1
                    r += 1
                    continue
                adj[word1[l]].add(word2[r])
                # adj[word1[l]].update(adj[word2[r]])
                return True
            if len(word2) < len(word1):
                return False
            return True
            
        for i in range(len(words)):
            if i + 1 < len(words):
                if not buildGraph(words[i], words[i+1]):
                    return ""
        print(adj)
        def build(key):
            nonlocal output
            if key in path:
                return False
            if key in visited:
                return True
            path.add(key)
            visited.add(key)

            for nei in adj[key]:
                if not build(nei):
                    return False
            path.remove(key)
            output = output + key
            return True

        output = ""
        visited = set()
        path = set()
        for key, value in adj.items():
            if not build(key):
                return ""

        return output[::-1]
