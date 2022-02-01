# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return None
        
        res = []
        dq = deque([root])
        
        while dq:
            total = 0
            n = len(dq)
            for _ in range(n):
                cur = dq.popleft()
                total += cur.val
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
            res.append(total / n)
            
        return res