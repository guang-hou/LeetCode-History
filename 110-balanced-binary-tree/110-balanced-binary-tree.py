# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return False
        else:
            return True
        
    def getDepth(self, node):
        if not node: return 0
        left_depth = self.getDepth(node.left)
        right_depth = self.getDepth(node.right)
        
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        else:
            return 1 + max(left_depth, right_depth)
        