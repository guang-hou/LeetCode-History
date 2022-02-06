# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder: return None
        
        if len(inorder) == len(postorder) == 1:
            return TreeNode(inorder[0])
        
        root_val = postorder[-1]
        inorder_root_index = inorder.index(root_val)
        
        inorder_left_tree = inorder[:inorder_root_index]
        inorder_right_tree = inorder[inorder_root_index + 1 :]
        postorder_left_tree = postorder[:inorder_root_index]
        postorder_right_tree = postorder[inorder_root_index : -1]
        left_node = self.buildTree(inorder_left_tree, postorder_left_tree)
        right_node = self.buildTree(inorder_right_tree, postorder_right_tree)
        
        return TreeNode(root_val, left_node, right_node)