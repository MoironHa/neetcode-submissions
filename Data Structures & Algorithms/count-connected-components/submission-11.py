class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        count = 0
        def bfs(i):
            queue = deque()
            queue.append(i)
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for nei in adj[node]:
                    if nei in visited:
                        continue
                    queue.append(nei)
                
        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)
        return count