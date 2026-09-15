class Solution:
    def numDecodings(self, s: str) -> int:

        def helper(i):
            if i in cache:
                return cache[i]
            nums = 0
            if i == len(s):
                return 1
            num = int(s[i])
            if num == 0:
                return 0
            if num > 0 and num < 10:
                nums += helper(i+1)
            if i + 2 <= len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                    nums += helper(i+2)
            cache[i] = nums
            return nums
        cache = {}
        return helper(0)