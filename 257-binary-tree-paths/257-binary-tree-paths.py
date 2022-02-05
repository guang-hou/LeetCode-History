# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        tmp = []
        
        def traversal(node):
            if not node: return None
            
            tmp.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(tmp))
                return
            
            if node.left:
                traversal(node.left)
                tmp.pop()
            if node.right:
                traversal(node.right)
                tmp.pop()
        
        traversal(root)
        
        return res
            
            
        
        
        
        