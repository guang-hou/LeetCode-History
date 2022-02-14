# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return None
        
        res = []
        path = []
        
        def traverse(node):
            if not node: return None
            
            path.append(node.val)
            
            if not node.left and not node.right and sum(path) == targetSum:
                res.append(path[:])

            if node.left:
                traverse(node.left)
                path.pop()
                
            if node.right:
                traverse(node.right)
                path.pop()
        
        traverse(root)
        
        return res