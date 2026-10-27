class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        currMax = 0
        curr = 0

        for R in range(len(prices)):
            if prices[R] > prices[L]:
                currMax += prices[R] - prices[L]
            L = R
        return currMax