class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = {}
        
        for char in magazine:
            record[char] = record.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in record:
                return False
            else:
                record[char] -= 1
                if record[char] < 0:
                    return False
        
        for v in record.values():
            if v < 0:
                return False
        
        return True