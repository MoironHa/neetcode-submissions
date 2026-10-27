class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr) <= 1:
                return arr
            m = len(arr) // 2
            left = merge(arr[:m])
            right = merge(arr[m:])
            res = []
            while left and right:
                if left[0] < right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            return res + left + right
        
        return merge(nums)