class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        count = len(nums) / 3
        res = []
        for num in nums:
            if num in res:
                continue
            hashmap[num] += 1
            if hashmap[num] > count:
                res.append(num)
        return res