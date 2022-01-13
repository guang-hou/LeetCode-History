class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = {}
        
        for char in words[0]:
            common[char] = common.get(char, 0) + 1
        
        for word in words[1:]:
            count = {}
            for char in word:
                count[char] = count.get(char, 0) + 1
            
            for char in common:
                if char not in count:
                    common[char] = 0
                else:
                    common[char] = min(common[char], count[char])
        
        res = []
        
        for char in common:
            if common[char] != 0:
                res.extend([char] * common[char])
        
        return res