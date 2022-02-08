# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root and not root.left and not root.right: return True
        
        res = []

        def traverse(node):
            if not node: return None
            
            if node.left: traverse(node.left)
            res.append(node.val)
            if node.right: traverse(node.right)

        traverse(root)
        
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        
        return True