class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        count = len(nums) / 3
        for num in nums:
            hashmap[num] += 1
        
        res = []
        for key, value in hashmap.items():
            if value > count:
                res.append(key)

        return res