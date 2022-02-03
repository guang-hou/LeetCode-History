# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def get_depth(node):
            if node and not node.left and not node.right: return 1
            if not node: return float("inf")
            
            return min(get_depth(node.left), get_depth(node.right)) + 1
    
        return get_depth(root)
        