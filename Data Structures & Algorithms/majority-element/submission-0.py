class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        res = nums[0]
        for key, value in hashmap.items():
            if value > hashmap[res]:
                res = key
        return res