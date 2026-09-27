class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        carry = 0
        output = 0

        for i in range(32):
            a_bit = a & 1
            b_bit = b & 1

            sum_bit = a_bit ^ b_bit ^ carry

            carry = (
                (a_bit & b_bit)
                | (a_bit & carry)
                | (b_bit & carry)
            )

            if sum_bit:
                output |= 1 << i

            a >>= 1
            b >>= 1

        if output > MAX_INT:
            output -= 0x100000000

        return output
