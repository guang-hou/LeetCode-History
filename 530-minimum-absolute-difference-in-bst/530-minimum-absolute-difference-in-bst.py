# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        
        def add_left(node):
            while node:
                stack.append(node)
                node = node.left
                
        add_left(root)
        
        res = float("inf")
        pre = None
        while stack:
            cur = stack.pop()
            if pre and abs(cur.val - pre.val) < res:
                res = abs(cur.val - pre.val)
            pre = cur
            
            if cur.right:
                add_left(cur.right)
        
        return res