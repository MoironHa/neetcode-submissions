class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        if length == 1:
            return True
        l = 0
        r = length - 1
        def rec(l, r, deleted):
            if l < r:
                if s[l] == s[r]:
                    if rec(l + 1, r -1, deleted):
                        return True
                    return False
                if deleted == 0 and (rec(l + 1, r, deleted + 1) or rec(l, r - 1, deleted + 1)):
                    return True
                return False
            return True
        return rec(l, r, 0)
             