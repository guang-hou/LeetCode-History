# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        res = []
        dq = deque([root])
        
        while dq:
            max_value = dq[0].val
            
            for _ in range(len(dq)):
                cur = dq.popleft()
                if cur.val > max_value: max_value = cur.val
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
            res.append(max_value)
            
        return res
        