# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        dq = deque([root])
        res = 0
        
        while dq:
            size = len(dq)
            res += 1
            
            for _ in range(size):
                cur = dq.popleft()
                if not cur.left and not cur.right:
                    return res
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)