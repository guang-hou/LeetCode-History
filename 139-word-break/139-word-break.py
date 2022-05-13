class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        record = {}
        
        def is_inside(s, wordDict, record):
            if s in wordDict: 
                record[s] = True
                return True
            if s in record:
                return record[s]
            
            if len(s) == 1: 
                record[s] = False
                return False

            for i in range(1, len(s)):
                left, right = s[:i], s[i:]

                is_left_inside = is_inside(left, wordDict, record)
                is_right_inside = is_inside(right, wordDict, record)
                
                if is_left_inside and is_right_inside:
                    record[s] = True
                    return True
                
            record[s] = False
            return False
        
        return is_inside(s, wordDict, record)