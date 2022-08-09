# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        middleIndex = len(nums) // 2
        middleElement = nums[middleIndex]
        
        root = TreeNode(middleElement)
        root.left = self.sortedArrayToBST(nums[:middleIndex])
        root.right = self.sortedArrayToBST(nums[middleIndex + 1:])
        
        return root
        