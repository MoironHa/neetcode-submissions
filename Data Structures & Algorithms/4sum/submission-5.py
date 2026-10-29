class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = []
        nums.sort()

        def check(first, second, third, fourth):
            ans = [first, second, third, fourth]
            ans.sort()
            if ans in seen:
                return
            res.append([first, second, third, fourth])
            seen.append(ans)

        for j, first in enumerate(nums):
            for i, second in enumerate(nums[j + 1:]):
                l = i + j + 2
                r = len(nums) - 1
                obj = target - first - second
                while l < r:
                    if nums[l] + nums[r] == obj:
                        check(first, second, nums[l], nums[r])
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < obj:
                        l += 1
                    else:
                        r -= 1
        
        return res