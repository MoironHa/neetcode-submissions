class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for i in nums:
            if i > 0 and i == res:
                res += 1
        return res