class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            curr = 0
            while i > 0:
                if i & 1 == 1:
                    curr += 1
                i = i // 2
            # curr += 1
            output.append(curr)
        return output