class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        def helper(i, subset):
            if i == len(nums):
                if subset == total / 2:
                    return True
                return False
            if (i + 1, subset) not in cache:
                cache[(i + 1, subset)] = helper(i + 1, subset + nums[i]) or helper(i + 1, subset)
                
            return cache[(i + 1, subset)]
        cache = {}
        return helper(0, 0)