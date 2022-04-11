class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval:(interval[0], interval[1]))
        res = []
        
        left, right = sorted_intervals[0]
        
        for i in range(1, len(sorted_intervals)):
            cur_left, cur_right = sorted_intervals[i]
            if cur_left <= right:
                right = max(right, cur_right)
            else:
                res.append([left, right])
                left, right = cur_left, cur_right
        
        res.append([left, right])
        
        return res
                    
        
        