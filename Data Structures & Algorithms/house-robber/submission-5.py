class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < n:
            tmp = dp[1]
            dp[1] = max(dp[1], dp[0] + nums[i])
            dp[0] = tmp
            i += 1
        return max(dp)