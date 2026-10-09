class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        visited = set()
        path = set()
        order = []
        for i in range(len(prerequisites)):
            b, a = prerequisites[i]
            if a == b:
                return []
            if b not in adjList:
                adjList[b] = []
            if a not in adjList:
                adjList[a] = []
            adjList[a].append(b)
        def dfs(course):
            nonlocal path, visited
            if course not in adjList:
                order.append(course)
                return True
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
            order.append(course)
            return True
        for a in range(numCourses):
            if not dfs(a):
                return []
            
        print(order)

        return order[::-1]