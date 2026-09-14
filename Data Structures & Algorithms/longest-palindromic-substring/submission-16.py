class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0, 1)
        length = len(s)
        curr = (0, 0)


        def helper(l, r, char):
            nonlocal res, curr
            curr =  (l, r)
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    curr = (l, r + 1)
                    if curr[1] - curr[0] > res[1] - res[0]:
                        res = curr
                else:
                    break
                l -= 1
                r += 1
        for i, char in enumerate(s):
            helper(i, i, char)
            helper(i, i+ 1, char)

        return s[res[0]:res[1]]
            