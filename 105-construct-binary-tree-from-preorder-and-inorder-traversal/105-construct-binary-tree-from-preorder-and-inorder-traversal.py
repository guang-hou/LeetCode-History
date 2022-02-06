# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        
        root_val = preorder[0]
        
        root_index = inorder.index(root_val)
        
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1:]
        preorder_left = preorder[1 : root_index + 1]
        preorder_right = preorder[root_index + 1:]
        
        root_left = self.buildTree(preorder_left, inorder_left)
        root_right = self.buildTree(preorder_right, inorder_right)
        
        root = TreeNode(root_val, root_left, root_right)
        
        return root