# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        # the nodehas value equals key
        if key == root.val:
            if not root.left and not root.right: 
                return None

            elif not root.left:
                return root.right

            elif not root.right:
                return root.left
            
            else:
                right = root.right
                while right.left:
                    right = right.left

                right.left = root.left
                return root.right

        # root val doesn't equal key, go down to its subnodes
        if key > root.val: root.right = self.deleteNode(root.right, key)
        elif key < root.val: root.left = self.deleteNode(root.left, key)
            
        return root