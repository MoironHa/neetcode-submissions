class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, (s, d) in enumerate(edges):
            adj[s].append((succProb[i], d))
            adj[d].append((succProb[i], s))
        
        heap = [(1, start_node)]
        shortest = {}
        while heap:
            w1, n1 = heapq.heappop_max(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for w2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush_max(heap, ((w1 * w2), n2))
        if end_node in shortest: 
            return shortest[end_node]
        return 0