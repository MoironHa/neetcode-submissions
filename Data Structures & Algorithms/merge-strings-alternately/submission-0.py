class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l = 0
        r = 0
        leftLength = len(word1)
        rightLength = len(word2)
        while l < leftLength and r < rightLength:
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1
        while l < leftLength:
            res.append(word1[l])
            l += 1
        while r < rightLength:
            res.append(word2[r])
            r += 1
        return "".join(res)