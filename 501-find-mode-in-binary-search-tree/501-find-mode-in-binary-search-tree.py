# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        pre = None
        max_count = 0
        count = 0

        tmp = [count, max_count, pre, res]

        
        def traverse(node):
            if not node: return None
            
            if node.left: traverse(node.left)
            
            if not tmp[2]:
                tmp[0] = 1
            elif node.val == tmp[2].val:
                tmp[0] += 1
            else:
                tmp[0] = 1

            if tmp[0] > tmp[1]:
                tmp[3] = [node.val]
                tmp[1] = tmp[0]
            elif tmp[0] == tmp[1]:
                tmp[3].append(node.val)
            
            tmp[2] = node
            
            if node.right: traverse(node.right) 
        
        traverse(root)
                
        return tmp[3]