class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, t in times:
            adj[u].append((t, v))
        print(adj)
        heap = [(0, k)]
        res = 0
        shortest = {}
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            res = max(res, w1)
            print(n1)
            print(adj[n1])
            for w2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, ((w1 + w2), n2))
        if len(shortest) == n:
            return res
        return -1