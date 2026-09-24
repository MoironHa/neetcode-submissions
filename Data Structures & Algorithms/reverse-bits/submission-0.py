class Solution:
    def reverseBits(self, n: int) -> int:
        output =  0
        i = 0
        while n > 0:
            if n & 1 == 1:
                output += 2 ** (31 - i)
            n = n >> 1
            i += 1
        return output