# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        elif not root1 and root2: return root2
        elif root1 and not root2: return root1
        
        stack = [root1, root2]
        
        while stack: # will not add None into stack
            cur2 = stack.pop()
            cur1 = stack.pop()
            
            cur1.val += cur2.val
            
            if cur2.right:
                if not cur1.right: cur1.right = TreeNode(0)
                stack.extend([cur1.right, cur2.right])
            
            if cur2.left:
                if not cur1.left: cur1.left = TreeNode(0)
                stack.extend([cur1.left, cur2.left])
                
        return root1