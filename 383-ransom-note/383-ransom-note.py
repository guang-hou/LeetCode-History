class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = {}
        
        for char in magazine:
            record[char] = record.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in record:
                return False
            else:
                if record[char] == 0:
                    return False
                else:
                    record[char] -= 1
        
        return True