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
        
        def swapInorderPredecessor(node):
            if not node.left and not node.right: 
                return None
            elif not node.left:
                return node.right
            else:
                inorder_pre = node.left
                prev = None
                while inorder_pre.right:
                    prev = inorder_pre
                    inorder_pre = inorder_pre.right
                
                if inorder_pre == node.left:
                    if node.right: inorder_pre.right = node.right

                else:
                    if inorder_pre.left:   
                        prev.right = inorder_pre.left
                    else:            # inorder predecessor has no left child, breake the link between prev and inorder_pre
                        prev.right = None
                    inorder_pre.left = node.left
                    if node.right: inorder_pre.right = node.right

                return inorder_pre
    
        
        if pre == None: return swapInorderPredecessor(cur)
                
        
        if right: pre.right = swapInorderPredecessor(cur)
        else: pre.left = swapInorderPredecessor(cur)
        return root