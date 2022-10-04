class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[0])
        res = 1
        
        leftEdge, rightEdge = points[0]
        
        for i in range(1, len(points)):
            leftX, rightX = points[i]
            if leftX > rightEdge:
                leftEdge, rightEdge = leftX, rightX
                res += 1
            else:
                leftEdge = max(leftEdge, leftX)
                rightEdge = min(rightEdge, rightX)
        
        return res