class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        prereqs = {}
        for i in range(numCourses):
            adj[i] = []
            prereqs[i] = set()
        for req, crs in prerequisites:
            adj[req].append(crs)
        def dfs(src, adj, visit, prereqs):
            if src in visit:
                return True
            visit.add(src)
            for course in adj[src]:
                dfs(course, adj, visit, prereqs)
                prereqs[src].add(course)
                prereqs[src].update(prereqs[course])
        
        visit = set()
        res = []
        for i in range(numCourses):
            dfs(i, adj, visit, prereqs)
        for u, v in queries:
            if v in prereqs[u]:
                res.append(True)
                continue
            res.append(False)
        return res