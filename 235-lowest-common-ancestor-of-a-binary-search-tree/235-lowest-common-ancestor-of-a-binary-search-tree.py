# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        
        if root.val >= low and root.val <= high: return root
        
        if root.val < low:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > high:
            return self.lowestCommonAncestor(root.left, p, q)
        
        