class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def helper(l, r, char):
            nonlocal res
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1
                r += 1
                
        for i, char in enumerate(s):
            helper(i, i, char)
            helper(i, i + 1, char)
        return res