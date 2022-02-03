# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        
        stack = []
        
        # LRS
        def add_left_right(node):
            while node:
                stack.append(node)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        
        add_left_right(root)
        
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if stack and stack[-1].right != cur:
                add_left_right(stack[-1].right)
                
        return root
                
        
        
        
        
