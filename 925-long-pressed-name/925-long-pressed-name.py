class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        
        while j < len(typed) and i < len(name):
            if typed[j] != name[i]:
                return False
            while j < len(typed) and i < len(name) and typed[j] == name[i]:
                j += 1
                i += 1
            
            while j < len(typed) and typed[j] == typed[j - 1]:
                j += 1
        
        return True if i == len(name) and j == len(typed) else False