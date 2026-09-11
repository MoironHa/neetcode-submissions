class Solution:
    def rob(self, nums: List[int]) -> int:
        ans1 = 0
        ans2 = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)


        dp = [nums[0], max(nums[0], nums[1])]
        i = 2

        while i < n-1:
            tmp = dp[1]
            dp[1] = max(dp[1], dp[0] + nums[i])
            dp[0] = tmp
            i += 1
        ans1 = dp[1]

        dp = [nums[1], max(nums[1], nums[2])]
        i = 3
        while i < n:
            tmp = dp[1]
            dp[1] = max(dp[1], dp[0] + nums[i])
            dp[0] = tmp
            i += 1
        ans2 = dp[1]


        return max(ans1, ans2)