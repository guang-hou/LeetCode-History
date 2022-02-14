# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        tmp = []
        
        def traverse(node):
            if not node: return None
            
            tmp.append(str(node.val))
            
            if not node.left and not node.right:
                res[0] += int("".join(tmp))
            
            if node.left: 
                traverse(node.left)
                tmp.pop()
            if node.right: 
                traverse(node.right)                
                tmp.pop()
        
        traverse(root)
        
        return res[0]