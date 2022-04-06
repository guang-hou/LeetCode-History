class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        path = []
        
        for i in range(len(s)):
            for j in range(len(s) - 1,i - 1, -1):
                if s[j] == s[i]:
                    path.append(j)
                    break

        start = 0
        largest = path[0]
        for i in range(0, len(path)):
            largest = max(largest, path[i])
            if i == largest:
                res.append(i + 1 - start)
                if i < len(path) - 1: 
                    largest = path[i + 1]
                    start = i + 1
        
        print(path)
        
        return res
            
            