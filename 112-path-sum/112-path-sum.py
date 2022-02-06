# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        path = []
        res = [False]
        
        def traverse(node):
            if not node: return None
            
            path.append(node.val)
            
            if not node.left and not node.right:
                if sum(path) == targetSum: 
                    res[0] = True
                    
            if node.left:
                traverse(node.left)
                path.pop()
            
            if node.right:
                traverse(node.right)
                path.pop()
            
        
        traverse(root)
            
        return res[0]
            
            