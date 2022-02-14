# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        res = []
        
        def traverse(node):
            if not node: return None
            if node.left: traverse(node.left)
            res.append(node)
            if node.right: traverse(node.right)
        
        traverse(root)
        
        current_sum = 0
        while res:
            cur = res.pop()
            current_sum += cur.val
            cur.val = current_sum
        
        return root