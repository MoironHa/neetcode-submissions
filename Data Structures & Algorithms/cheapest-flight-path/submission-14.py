class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, p in flights:
            adj[u].append((v, p))
        heap = [(0, -1, src)]
        best = {}
        while heap:
            p, stops, u = heapq.heappop(heap)
            state = (u, stops)
            if state in best:
                continue
            if u == dst and stops <= k:
                return p
            best[state] = p
            for v, price in adj[u]:
                if stops < k:
                    heapq.heappush(heap, (p + price, stops + 1, v))
        return -1