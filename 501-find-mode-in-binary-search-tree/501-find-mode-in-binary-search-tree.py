# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        
        res = []
        pre = None
        max_count = 0
        count = 0
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if not pre:
                    count = 1
                elif cur.val == pre.val:
                    count += 1
                else:
                    count = 1
                
                if count > max_count:
                    res = [cur.val]
                    max_count = count
                elif count == max_count:
                    res.append(cur.val)
                            
                pre = cur
                cur = cur.right
                
        return res