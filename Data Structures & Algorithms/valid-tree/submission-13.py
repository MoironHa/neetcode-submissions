class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n or len(edges) < n - 1:
            return False
        adjList = {}
        visited = set()
        for s, d in edges:
            if s not in adjList:
                adjList[s] = []
            if d not in adjList:
                adjList[d] = []
            adjList[s].append(d)
            adjList[d].append(s)
        print(adjList)
    
        def dfs(source, destination, parent):
            if source not in visited:
                visited.add(source)
            for d in destination:
                if d in visited and d != parent:
                    return False
                if d in visited:
                    continue
                visited.add(d)
                if not dfs(d, adjList[d], source):
                    return False
            return True
    
        return dfs(0, adjList.get(0, []), None) and len(visited) == n
            