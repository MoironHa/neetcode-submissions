class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * n
        for i in range(n-2, -1, -1):
            num = min(i + nums[i], n -1)
            best = arr[num]
            while num > i:
                best = min(best, arr[num])
                num -= 1
            arr[i] = best + 1
        return arr[0]
        