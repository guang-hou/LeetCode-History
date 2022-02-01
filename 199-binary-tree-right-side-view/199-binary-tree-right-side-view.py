# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        res = []
        dq = deque([root])
        
        while dq:
            n = len(dq)
            for i in range(n):
                cur = dq.popleft()
                if i == n - 1:
                    res.append(cur.val)
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
        return res
        