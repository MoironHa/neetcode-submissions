class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # adj = {}
        # for x, y in points:
        adj = points
        heap = [(0, points[0][0], points[0][1])]
        shortest = {}
        
        while heap and len(shortest) != len(points):
            print("once")
            w, x, y = heapq.heappop(heap)
            if (x, y) in shortest:
                continue
            shortest[(x, y)] = w
            
            for u, v in points:
                if (u, v) in shortest:
                    continue
                cost = abs(x - u) + abs(y - v)
                heapq.heappush(heap, (cost, u, v))
        res = 0
        for key, value in shortest.items():
            res += value
        return res