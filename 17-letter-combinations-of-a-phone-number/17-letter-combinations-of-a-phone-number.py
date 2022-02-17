class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return None
        
        mapping = {'2': ["a", "b", "c"], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], 
                   '9': ['w', 'x', 'y', 'z']}
        
        res = []
        path = []
        
        def backtrack(start, end):
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return
            
            for i in range(start, end):
                letters = mapping[digits[i]]
                for letter in letters:
                    path.append(letter)                        
                    backtrack(i + 1, end) # recursion
                    path.pop()
        
        backtrack(0, len(digits))
                           
        return res
