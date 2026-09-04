class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curSet = []
        nums = sorted(nums)
        print(nums)

        def helper(i, nums, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            curSet.append(nums[i])
            helper( i + 1, nums, subsets, curSet)
            curSet.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            helper( i + 1, nums, subsets, curSet)
        helper(0, nums, subsets, curSet)
        return subsets