class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            curLeft, curRight = intervals[i]
            lastLeft, lastRight = res[-1]
            
            if curLeft <= lastRight:
                res[-1] = [lastLeft, max(lastRight, curRight)]
            else:
                res.append(intervals[i])
        
        return res
                