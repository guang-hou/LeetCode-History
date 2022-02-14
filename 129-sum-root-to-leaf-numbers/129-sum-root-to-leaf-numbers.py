# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        tmp = [str(root.val)]
        
        def traverse(node):
            if not node: return None
            
            if not node.left and not node.right:
                res[0] += int("".join(tmp))
            
            if node.left: 
                tmp.append(str(node.left.val))
                traverse(node.left)
                tmp.pop()
            if node.right: 
                tmp.append(str(node.right.val))
                traverse(node.right)                
                tmp.pop()
        
        traverse(root)
        
        return res[0]