class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        curComb = []
        candidates.sort()

        def helper(i, curSum):
            # print(f"called with i: {i} and curSum: {curSum} and curComb: {curComb}")
            if curSum == target:
                # print(f"found a combo")
                combinations.append(curComb.copy())
                return
            if curSum > target or i >= len(candidates):
                return
            
            
            # for index in range(i, len(candidates)):
            num = candidates[i]
            curComb.append(num)
            helper(i + 1, curSum + num)
            curComb.pop()
            while i +1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            helper(i + 1, curSum)
        helper(0, 0)
        return combinations