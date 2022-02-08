# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        stack = []
        
        def add_left(node):
            while node:
                stack.append(node)
                node = node.left
        
        add_left(root)
        pre = None
        
        while stack:
            cur = stack.pop()
            if pre and cur.val <= pre.val:
                return False
            pre = cur
            
            if cur.right:
                add_left(cur.right)
            
        return True