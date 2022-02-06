# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def getLeft(node):
            if not node: return 0
            
            if node and node.left and not node.left.left and not node.left.right:
                return node.left.val + getLeft(node.right)
            
            return getLeft(node.left) + getLeft(node.right)
        
        return getLeft(root)