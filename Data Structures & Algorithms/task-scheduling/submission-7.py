class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        heap = [-count for count in Counter(tasks).values()]
        runs = 0
        queue = deque()
        heapq.heapify(heap)
        while heap or queue:
            while queue and queue[0][1] <= runs:
                neg_count, _ = queue.popleft()
                heapq.heappush(heap, neg_count)
            if heap: 
                neg_count = heapq.heappop(heap)
                runs += 1 
                if neg_count + 1 < 0:
                    queue.append((neg_count + 1, runs + n))
            else:
                # Nothing available; jump to next available task
                runs = queue[0][1]
        return runs                
        
