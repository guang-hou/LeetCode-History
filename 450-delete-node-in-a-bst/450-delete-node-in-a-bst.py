# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        # check if the node exists
        cur = root
        pre = None
        right = False
        while cur:
            if key > cur.val:
                pre = cur
                right = True
                cur = cur.right
            elif key < cur.val:
                pre = cur
                right = False
                cur = cur.left
            else:
                break
        
        if not cur: return root
        
        if not cur.left and not cur.right:
            if pre == None:
                return None
            else:
                if right: pre.right = None
                else: pre.left = None
        if cur.left and not cur.right:
            if pre == None:
                return cur.left
            else:
                if right: pre.right = cur.left
                else: pre.left = cur.left
            
        if not cur.left and cur.right:
            if pre == None:
                return cur.right
            else:
                if right: pre.right = cur.right
                else: pre.left = cur.right
            
        if cur.left and cur.right:
            if pre == None:
                if not cur.right.left:
                    cur.right.left = cur.left
                    return cur.right
                else:
                    right_left = cur.right.left
                    while right_left.left:
                        right_left = right_left.left
                    right_left.left = cur.left
                    return cur.right
            else:
                if not cur.right.left:
                    cur.right.left = cur.left
                    if right: pre.right = cur.right
                    else: pre.left = cur.right

                else:
                    right_left = cur.right.left
                    while right_left and right_left.left:
                        right_left = right_left.left
                    right_left.left = cur.left
                    if right: pre.right = cur.right
                    else: pre.left = cur.right
        
        return root