# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traversal(node):
            nonlocal res
            
            if not node: return 2
            
            left = traversal(node.left)
            right = traversal(node.right)
            

            if left == 2 and right == 2:
                return 0
            
            elif left == 0 or right == 0:
                res += 1
                return 1
            
            elif left == 1 or right == 1:
                return 2
            
        
        if traversal(root) == 0:
            res += 1
        
        return res
            