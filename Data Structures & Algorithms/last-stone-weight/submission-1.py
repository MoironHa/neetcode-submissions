class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        
        while len(maxHeap) > 1:
            x = heapq.heappop_max(maxHeap)
            y = heapq.heappop_max(maxHeap)

            if x > y:
                x = x - y
                heapq.heappush_max(maxHeap, x)
            elif x < y:
                y = y - x
                heapq.heappush_max(maxHeap, y)
    
        if len(maxHeap) == 1:
            return maxHeap[0]
        else:
            return 0
