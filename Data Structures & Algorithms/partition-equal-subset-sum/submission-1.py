class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def helper(i, subset1, subset2):
            if i == len(nums):
                if subset1 == subset2:
                    return True
                return False
            if (i + 1, subset1, subset2) not in cache:
                cache[(i + 1, subset1, subset2)] = helper(i + 1, subset1 + nums[i], subset2) or helper(i + 1, subset1, subset2 + nums[i])
                
            return cache[(i + 1, subset1, subset2)]
        cache = {}
        return helper(0, 0, 0)