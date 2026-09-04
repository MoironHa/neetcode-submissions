class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combinations = []
        curComb = []
        hashmap = {}
        hashmap['2'] = 'abc'
        hashmap['3'] = 'def'
        hashmap['4']= 'ghi'
        hashmap['5'] = 'jkl'
        hashmap['6'] = 'mno'
        hashmap['7'] = 'pqrs'
        hashmap['8'] = 'tuv'
        hashmap['9'] = 'wxyz'

        def helper(start):
            if len(curComb) == len(digits):
                combinations.append(''.join(curComb.copy()))
                return
            letters = hashmap[digits[start]]
            for letter in letters:
                curComb.append(letter)
                helper(start + 1)
                curComb.pop()
        helper(0)
        return combinations


        
