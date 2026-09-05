class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        openParen = 0
        closeParen = 0
        def helper(curComb):
            nonlocal openParen, closeParen, combinations
            if openParen == closeParen == n:
                combinations.append(curComb)
                return
            if openParen < n:
                openParen += 1
                helper(curComb + '(')
                openParen -= 1
            if closeParen < openParen:
                closeParen += 1
                helper(curComb + ')')
                closeParen -= 1
            
        helper('')
        return combinations