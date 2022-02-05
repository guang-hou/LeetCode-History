# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        stack = [root]
        tmp = []
        
        while stack:
            cur = stack.pop()
            if cur:
                tmp.append(str(cur.val))
                if not cur.left and not cur.right:
                    res.append("->".join(tmp))
                    tmp.pop()
                else:
                    stack.append(None)
                
                if cur.right: stack.append(cur.right)
                if cur.left: stack.append(cur.left)
            else:
                tmp.pop()
            
        return res
        
        