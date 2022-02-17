class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return None
        
        mapping = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
        
        res = []
        path = []
        
        def backtrack(start, end):
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return
            
            for i in range(start, end - (len(digits) - len(path) - 1)):
                letters = mapping[digits[i]]
                for letter in letters:
                    path.append(letter)                        
                    backtrack(i + 1, end) 
                    path.pop()
        
        backtrack(0, len(digits))
                           
        return res
