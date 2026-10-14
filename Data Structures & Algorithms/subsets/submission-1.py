class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets, curSet = [], []
        

        def helper(i, nums, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            helper(i + 1, nums, subsets, curSet)
            curSet.pop()
            helper(i + 1, nums, subsets, curSet)
            
        helper(0, nums, subsets, curSet)
        return subsets
        