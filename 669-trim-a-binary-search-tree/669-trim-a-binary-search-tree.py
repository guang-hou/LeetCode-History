# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        if root.val < low or root.val > high:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif not root.left and root.right:
                return root.right
            else:
                right_left = root.right
                while right_left.left:
                    right_left = right_left.left
                
                right_left.left = root.left
                return root.right
        
        return root