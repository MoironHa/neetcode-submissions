class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = nums[n-1]
        for i in range(n-1):
            xorr ^= nums[i]
        return xorr