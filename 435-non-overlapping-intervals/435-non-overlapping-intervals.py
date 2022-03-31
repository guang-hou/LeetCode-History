class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        new_intervals = sorted(intervals)
        l, r = new_intervals[0]
        res = 0
        
        for i in range(1, len(new_intervals)):
            left, right = new_intervals[i]
            
            if left >= r:
                l, r = left, right
                continue
                
            if right < r:
                res += 1
                l, r = left, right
            else:
                res += 1
        
        return res
        
        