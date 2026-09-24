class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = len(nums)
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr