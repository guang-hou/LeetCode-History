# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        
        stack = []
        
        def traverse(node):
            if node.left: traverse(node.left)
            
            stack.append(node)
                
            if node.right: traverse(node.right)
                
        traverse(root)
        
        def createTree(stack):
            if not stack: return None
            root = stack[len(stack) // 2]
        
            root.left = createTree(stack[: len(stack) // 2])
            root.right = createTree(stack[len(stack) // 2 + 1 : ])
            return root
        
        root = createTree(stack)
        
        return root