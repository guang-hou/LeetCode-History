# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        stack = []
        res = []
        
        def add_left(node):
            while node:
                pre = node
                stack.append(node)
                node = node.left
                if not node:
                    node = pre.right
        
        add_left(root)
        
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if stack and stack[-1].right != cur: 
                add_left(stack[-1].right)
                    
        return res
        
        
            