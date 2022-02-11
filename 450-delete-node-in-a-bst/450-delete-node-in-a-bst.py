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
        right = False  # track if pre.right = cur
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
        
        def deleteNode(node):
            if not node.left and not node.right: 
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                right_left = node.right
                while right_left.left:
                    right_left = right_left.left
                
                right_left.left = node.left
                
                return node.right
    
        
        if pre == None: return deleteNode(cur)
                
        
        if right: pre.right = deleteNode(cur)
        else: pre.left = deleteNode(cur)
        return root