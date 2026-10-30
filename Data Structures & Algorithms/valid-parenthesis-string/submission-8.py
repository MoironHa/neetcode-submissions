class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []

        for i, char in enumerate(s):
            if char == "(":
                left.append((i, char))
            elif char == ")":
                if left:
                    left.pop()
                elif stars and stars[0] < i:
                    stars.pop(0)
                else:
                    return False
            else:
                stars.append(i)

        while left and stars:
            star = stars.pop()
            par = left.pop()[0]
            if star > par:
                continue
            else:
                return False


        return not left