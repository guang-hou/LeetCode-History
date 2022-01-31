# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        
        dq = deque()
        res = []
        
        dq.append(root)
        
        while dq:
            n = len(dq)
            tmp = []
            for _ in range(n):
                cur = dq.popleft()
                tmp.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            res.append(tmp)
            
        return res