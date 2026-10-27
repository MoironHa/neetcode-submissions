class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1
        for _ in range(len(nums)):
            if res in nums:
                res += 1
        return res