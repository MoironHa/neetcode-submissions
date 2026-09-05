class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            while i +1 < len(nums) and nums[i+1] == nums[i]:
                nums.remove(nums[i+1])
        return len(nums)