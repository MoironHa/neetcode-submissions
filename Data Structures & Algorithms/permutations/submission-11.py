class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        curComb = []

        def helper(i):
            # print(f"called with: {curComb} and i: {i}")
            if i >= len(nums):
                if len(curComb) == len(nums):
                    combinations.append(curComb.copy())
                return
            
            for num in nums:
                if num not in curComb:
                    curComb.append(num)
                    helper(i+1)
                    curComb.pop()
                helper(i+1)
                
        helper(0)
        return combinations