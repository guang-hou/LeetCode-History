class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        mapToInt = {
            '(' : 1,
            ')' : -1,
            '{': 2,
            '}': -2,
            '[': 3,
            ']': -3
        }
        
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                
                ele = stack.pop()
                
                if mapToInt[ele] != -mapToInt[char]:
                    return False
        
        return not stack