class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if i > 0 and (num == nums[i - 1]):
                continue
            target = num * -1
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if (nums[left] + nums[right] == target):
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                elif (nums[left] + nums[right] < target):
                    left += 1
                else:
                    right -= 1
        return ans
