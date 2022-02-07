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
        
#         stack = [root1, root2]
        
#         while stack:
#             cur2 = stack.pop()
#             cur1 = stack.pop()
            
#             if cur2 and cur1:
#                 cur1.val += cur2.val
#             elif cur2 and not cur1:
                
        def traverse(root1, root2):
            if not root2: return None      
            
            root1.val += root2.val
            
            if root2.right: 
                if not root1.right:
                    root1.right = TreeNode(0)
                    
                traverse(root1.right, root2.right)
            
            if root2.left: 
                if not root1.left: 
                    root1.left = TreeNode(0)
                    
                traverse(root1.left, root2.left)
        
        traverse(root1, root2)
        
        return root1