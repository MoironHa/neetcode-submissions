class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        num = abs(x)
        res = 0
        i = (10 ** (len(str(num)) - 1))

        while num > 0:
            digit = num % 10
            res += digit * i
            num = num // 10
            i = i // 10
        if res > 0x7FFFFFFF:
            return 0
        if x > 0:
            return res
        if x < 0:
            return -res
