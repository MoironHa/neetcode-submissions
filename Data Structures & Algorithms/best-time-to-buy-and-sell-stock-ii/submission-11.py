class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        currMax = 0
        curr = 0

        for R in range(1, len(prices)):
            if prices[R] > prices[R - 1]:
                currMax += prices[R] - prices[R - 1]
        return currMax