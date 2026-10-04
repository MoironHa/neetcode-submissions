class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visited = set()
        path = set()
        for i in range(len(prerequisites)):
            b, a = prerequisites[i]
            if a == b:
                return False
            if b not in adjList:
                adjList[b] = []
            if a not in adjList:
                adjList[a] = []
            adjList[a].append(b)
        def dfs(course):
            nonlocal path, visited
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for b in adjList[course]:                    
                if not dfs(b):
                    return False
            path.remove(course)
            visited.add(course)
            return True
        for a in adjList:
            if not dfs(a):
                return False
    
        return True