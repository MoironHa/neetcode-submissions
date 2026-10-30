class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 1:
            return 0 if gas[0] >= cost[0] else -1 
        i = 0
        while i < n:
            tank = gas[i] - cost[i]
            visited = 0
            j = i

            while tank >= 0 and visited < n - 1:
                tank = tank + gas[(j + 1) % n] - cost[(j + 1) % n]
                visited += 1
                j += 1
                if tank >= 0 and visited >= n - 1:
                    return i
            i = j + 1
        return -1