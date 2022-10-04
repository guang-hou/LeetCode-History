class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[0])
        res = 1
        
        rightEdge = points[0][1]
        
        for i in range(1, len(points)):
            x_start, x_end = points[i]
            if x_start > rightEdge:
                rightEdge = x_end
                res += 1
            else:
                rightEdge = min(rightEdge, x_end)
        
        return res