# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        if root and not root.left and not root.right:
            if targetSum == root.val: return True
            else: return False

        left_res, right_res = False, False

        if root.left:
            left_res = self.hasPathSum(root.left, targetSum - root.val)

        if root.right:
            right_res = self.hasPathSum(root.right, targetSum - root.val)

        return left_res or right_res
            
            