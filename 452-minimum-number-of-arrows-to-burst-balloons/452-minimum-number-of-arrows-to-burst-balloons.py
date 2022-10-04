class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[0])
        res = 1
        
        leftEdge, rightEdge = points[0]
        
        for i in range(1, len(points)):
            x_start, x_end = points[i]
            if x_start > rightEdge:
                leftEdge, rightEdge = x_start, x_end
                res += 1
            else:
                leftEdge = max(leftEdge, x_start)
                rightEdge = min(rightEdge, x_end)
        
        return res