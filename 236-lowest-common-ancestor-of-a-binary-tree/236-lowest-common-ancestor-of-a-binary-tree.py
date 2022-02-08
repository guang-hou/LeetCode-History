# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(node):
            has_p, has_q = False, False
            
            if not node: return (None, False, False)
            if node.val == p.val:
                has_p = True
            if node.val == q.val:
                has_q = True
            
            left_res = right_res = (None, False, False)
            
            if node.left:
                left_res = traverse(node.left)
                if left_res[1] and left_res[2]: return left_res
            if node.right:
                right_res = traverse(node.right)
                if right_res[1] and right_res[2]: return right_res
                
            has_p = has_p or left_res[1] or right_res[1]
            has_q = has_q or left_res[2] or right_res[2]
            
            
            return (node, has_p, has_q)
        
        res = traverse(root)
        return res[0]