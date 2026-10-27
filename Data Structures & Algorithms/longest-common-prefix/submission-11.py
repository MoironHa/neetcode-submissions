class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x:len(x))
        res = ""
        for i, letter in enumerate(strs[0]):
            for word in strs:
                if word[i] != letter:
                    return res
            res += letter
        return res