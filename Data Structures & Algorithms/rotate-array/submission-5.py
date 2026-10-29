class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        def reverse(l, r):
            while l < r:
                tmp = nums[r]
                nums[r] = nums[l]
                nums[l] = tmp
                l += 1
                r -= 1
        reverse(0, length - 1)
        reverse(0, k%length - 1)
        reverse(k%length, length - 1)