class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cache = {}

        maxP = nums[0]
        minP = nums[0]


        for x in range(1, len(nums)):
            maxP = maxP * nums[x]
            minP = minP * nums[x]
            
            tmp = maxP
            maxP = max(nums[x], maxP, minP)
            minP = min(nums[x], tmp, minP)

            if maxP > res:
                res = maxP

        return res