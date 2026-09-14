class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        length = len(s)


        def helper(l, r, char):
            nonlocal res
            curr =  char
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    curr = s[l:r+1]
                    if len(curr) > len(res):
                        res = curr
                else:
                    break
                l -= 1
                r += 1
        for i, char in enumerate(s):
            helper(i, i, char)
            helper(i, i+ 1, char)
        return res
            