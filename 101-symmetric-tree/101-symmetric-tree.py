# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        stack = [root.left, root.right]  
        
        while stack:
            cur1 = stack.pop()
            cur2 = stack.pop()
            if cur1 and not cur2 or not cur1 and cur2:
                return False
            elif cur1 and cur2:
                if cur1.val != cur2.val:
                    return False
                else:
                    stack.append(cur1.left)
                    stack.append(cur2.right)
                    stack.append(cur1.right)
                    stack.append(cur2.left)
            
        return True
