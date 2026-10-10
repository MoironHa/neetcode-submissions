class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(len(edges) + 1)]
        def dfs(u, v):
            if v in adj[u] or u in adj[v]:
                return True
            adj[u].add(v)
            adj[v].add(u)
            newSet = set()
            newSet.add(u)
            newSet.add(v)
            for nei in adj[u]:
                newSet.add(nei)
            for nei in adj[v]:
                newSet.add(nei)
            for nei in adj[u]:
                adj[nei] = newSet
            for nei in adj[v]:
                adj[nei] = newSet
            return False

        for u, v in edges:
            if dfs(u, v):
                return [u, v]