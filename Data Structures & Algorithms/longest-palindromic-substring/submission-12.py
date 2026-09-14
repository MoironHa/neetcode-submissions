class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        length = len(s)


        def helper(l, r, char):
            nonlocal res
            curr =  1
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    curr = (l, r + 1)
                    if curr[1] - curr[0] > len(res):
                        res = s[curr[0]:curr[1]]
                else:
                    break
                l -= 1
                r += 1
        for i, char in enumerate(s):
            helper(i, i, char)
            helper(i, i+ 1, char)
        return res
            