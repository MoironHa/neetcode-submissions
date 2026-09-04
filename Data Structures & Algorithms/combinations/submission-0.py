class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        curComb = []

        def back(i, n, combinations, curComb):
            if len(curComb) >= k:
                combinations.append(curComb.copy())
                return
            if i <= n:
                curComb.append(i)
            else:
                return
            back(i + 1, n, combinations, curComb)
            curComb.pop()
            back(i + 1, n, combinations, curComb)
        back(1, n, combinations, curComb)
        return combinations