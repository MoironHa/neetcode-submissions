class Solution:
    def partition(self, s: str) -> List[List[str]]:
        combinations = []
        curComb = []

        def isPalindrome(string):
            if len(string) == 1:
                print(string)
                return True
            elif len(string) < 1:
                return False
            l = 0
            r = len(string) - 1
            while l < r:
                if string[l] == string[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            print(string)
            return True

        def helper(i):
            if i == len(s):
                print(f"adding to combinations")
                combinations.append(curComb.copy())
                return 
            for j in range(i, len(s)):
                subString = s[i:j+1]
                if isPalindrome(subString):
                    curComb.append(subString)
                    helper(j+1)
                    curComb.pop()
                
        helper(0)
        return combinations