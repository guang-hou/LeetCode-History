# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            if not root:
                return (0, 0)

            left = traverse(root.left)    # 1X2 array, left[0] not rob root.left, left[1]rob root.left
            right = traverse(root.right)

            not_rob_root = max(left) + max(right)
            rob_root = root.val + left[0] + right[0]
            
            return (not_rob_root, rob_root)
        
        res = traverse(root)
        
        return max(res)