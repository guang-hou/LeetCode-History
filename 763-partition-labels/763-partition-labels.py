class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        path = []
        
        def getLastIndex(start):
            for i in range(len(s) - 1,start, -1):
                if s[i] == s[start]:
                    return i
            return start    
        
        for i in range(len(s)):
            last_index = getLastIndex(i)
            path.append(last_index)
        
        start = 0
        largest = path[0]
        for i in range(0, len(path)):
            if path[i] > largest:
                largest = path[i]
            if i == largest:
                res.append(i + 1 - start)
                if i < len(path) - 1: 
                    largest = path[i + 1]
                    start = i + 1
        
        print(path)
        
        return res
            
            