class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = set()
        good.add(len(nums) - 1)
        for i in range(len(nums)-2, -1, -1):
            num = i + nums[i]
            while num > i:
                if num in good:
                    good.add(i)
                num -= 1
        return 0 in good