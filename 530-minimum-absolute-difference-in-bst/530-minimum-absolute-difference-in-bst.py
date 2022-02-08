# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        
        res = float("inf")
        pre = None

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and abs(cur.val - pre.val) < res:
                    res = abs(cur.val - pre.val)
                pre = cur
                cur = cur.right

        
        return res