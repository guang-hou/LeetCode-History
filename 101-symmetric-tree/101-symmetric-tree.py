# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: return True
        elif root.left and not root.right: return False
        elif not root.left and root.right: return False
        
        stack1 = [root.left]  # SLR
        stack2 = [root.right] # SRL
        
        while stack1 and stack2:
            cur1 = stack1.pop()
            cur2 = stack2.pop()
            if cur1.val != cur2.val:
                return False
            if (cur1.right and not cur2.left) or (cur1.left and not cur2.right):
                return False
            elif cur1.right and cur2.left and cur1.right.val != cur2.left.val:
                return False
            elif cur1.left and cur2.right and cur1.left.val != cur2.right.val:
                return False
            
            if cur1.right: stack1.append(cur1.right)
            if cur1.left: stack1.append(cur1.left)
            
            if cur2.left: stack2.append(cur2.left)
            if cur2.right: stack2.append(cur2.right)
            
        
        if not stack1 and not stack2: return True
        else: return False