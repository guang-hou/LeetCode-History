class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        xs, xe = -float('inf'), float('inf')
        res = 1

        for x1, x2 in points:
            xs = max(xs, x1)
            xe = min(xe, x2)
            
            if xs > xe:
                res += 1
                xs, xe = x1, x2
        
        return res
            