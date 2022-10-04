# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    
    def traverse(self, node):
        if not node:
            return 2
        
        left, right = self.traverse(node.left), self.traverse(node.right)
        
        if left ==2 and right ==2:
            return 0
        elif left == 0 or right == 0:
            self.res += 1
            return 1
        elif left == 1 or right == 1:
            return 2
        
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if self.traverse(root) == 0:
            self.res += 1
        
        return self.res