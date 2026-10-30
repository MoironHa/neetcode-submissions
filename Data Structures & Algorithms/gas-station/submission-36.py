class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        totalgas = 0
        startindex = 0

        for i in range(len(gas)):
            totalgas += gas[i] - cost[i]
            if totalgas < 0:
                totalgas = 0
                startindex = i + 1
        return startindex