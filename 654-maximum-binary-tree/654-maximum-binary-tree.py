# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        
        root_val = max(nums)
        index = nums.index(root_val)
        prefix = nums[:index]
        suffix = nums[index + 1:]
        
        left_node = self.constructMaximumBinaryTree(prefix)
        right_node = self.constructMaximumBinaryTree(suffix)
        
        root = TreeNode(root_val, left_node, right_node)
        
        return root