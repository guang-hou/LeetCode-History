# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        res = 0
        
        while dq:
            size = len(dq)
            res = dq[0].val
            
            for _ in range(size):
                cur = dq.popleft()
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
            
            
        return res