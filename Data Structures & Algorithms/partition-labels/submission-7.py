class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        order = []
        seen = set()
        res = []
        hashmap = defaultdict(list)
        for i, char in enumerate(s):
            if char not in seen:
                order.append(char)
                seen.add(char)
            hashmap[char].append(i)
        last = 0
        first = 0
        size = 1
        for char in order:
            if hashmap[char][0] > last:
                res.append(last - first + 1)
                first = hashmap[char][0]
            last = max(last, hashmap[char][len(hashmap[char]) - 1])
        res.append(last - first + 1)
        return res
            
            
