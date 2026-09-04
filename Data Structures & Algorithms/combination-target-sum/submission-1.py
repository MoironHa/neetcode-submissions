class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        curComb = []
        def helper(curSum, start):            
            if curSum == target:
                combinations.append(curComb.copy())
                return
            if curSum > target:
                return
            
            
            for i in range(start, len(nums)):
                curComb.append(nums[i])
                helper(curSum + nums[i], i)
                curComb.pop()
        helper(0, 0)
        return combinations