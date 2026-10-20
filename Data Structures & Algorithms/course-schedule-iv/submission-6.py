class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        prereqs = {}
        for i in range(numCourses):
            adj[i] = []
            prereqs[i] = set()
        for req, crs in prerequisites:
            adj[req].append(crs)
        # def update(prereqs):
        #     queue = deque()
        #     queue.append(src)
        #     while queue:
        #         srcs = queue.popleft()
        #         for course in adj[srcs]:
        #             prereqs[srcs].add(course)
        #             for req in prereqs[course]:
        #                 prereqs[srcs].add(req)
        #             queue.append(course)
        def dfs(src, adj, visit, topSort, prereqs):
            if src in visit:
                return True
            visit.add(src)
            for course in adj[src]:
                dfs(course, adj, visit, topSort, prereqs)
                prereqs[src].add(course)
                prereqs[src].update(prereqs[course])
            topSort.append(src)
            
        
        topSort = []
        visit = set()
        res = []
        for i in range(numCourses):
            dfs(i, adj, visit, topSort, prereqs)
        for u, v in queries:
            if v in prereqs[u]:
                res.append(True)
                continue
            res.append(False)
        return res