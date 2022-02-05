# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node1, node2):
            if not node1 and not node2:
                return True
            elif (not node1 and node2) or (node1 and not node2):
                return False
            elif node1.val != node2.val:
                return False
            
            left_right = traverse(node1.left, node2.right)
            right_left = traverse(node1.right, node2.left)
    
            return left_right and right_left
        
        return traverse(root.left, root.right)
            
            
            
