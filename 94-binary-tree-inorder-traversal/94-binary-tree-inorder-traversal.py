# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        res = []
        
        def traversal(node):
            if not node: return None
            
            traversal(node.left)
            res.append(node.val)
            traversal(node.right)
        
        traversal(root)
        
        return res