# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            if not root:
                #print("None node")
                return (0, 0)
            
            left, right = [0, 0], [0, 0]
            if root.left:
                left = traverse(root.left)    # 1X2 array, left[0] not rob root.left, left[1]rob root.left
            if root.right:
                right = traverse(root.right)
            
            # print("root", root)
            # print("left", left)
            # print("right", right)

            not_rob_root = max(left) + max(right)
            rob_root = root.val + left[0] + right[0]
            
            res = [not_rob_root, rob_root]
            # print("return", res)
            return res
        
        res = traverse(root)
        
        return max(res)