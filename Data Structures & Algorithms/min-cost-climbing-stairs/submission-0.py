class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost)
        
        dp = [cost[0], cost[1]]
        i = 2
        while i < n:
            tmp = dp[1]
            dp[1] = min(dp[0] + cost[i], dp[1] + cost[i])
            dp[0] = tmp
            i += 1

        return min(dp[0], dp[1])