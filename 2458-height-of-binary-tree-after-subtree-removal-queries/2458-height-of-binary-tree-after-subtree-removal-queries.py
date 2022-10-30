# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depthMap, heightMap = defaultdict(int), defaultdict(int)
        TwoHighestNodesAtdepth = defaultdict(list)
        
        self.traverse(root, 0, depthMap, heightMap)
        
        for val, depth in depthMap.items():
            TwoHighestNodesAtdepth[depth].append(val)
            TwoHighestNodesAtdepth[depth].sort(key = lambda a : -heightMap[a]) 
            
            if len(TwoHighestNodesAtdepth[depth]) > 2:
                TwoHighestNodesAtdepth[depth].pop()
        
        ans = []
        origHeight = heightMap[root.val]
        
        for target in queries:
            depth = depthMap[target]
            #print(TwoHighestNodesAtdepth[depth])

            if len(TwoHighestNodesAtdepth[depth]) == 1:  # root node, or single leaf node
                ans.append(depth - 1)
            elif len(TwoHighestNodesAtdepth[depth]) == 2 and TwoHighestNodesAtdepth[depth][0] == target:
                otherNode = TwoHighestNodesAtdepth[depth][1]
                ans.append(depth + heightMap[otherNode])
            else:
                ans.append(origHeight)
        
        return ans
        
    def traverse(self, node, depth, depthMap, heightMap):
        if not node:
            return -1
        
        depthMap[node.val] = depth
        
        leftHeight = self.traverse(node.left, depth + 1, depthMap, heightMap)
        rightHeight = self.traverse(node.right, depth + 1, depthMap, heightMap)
        myHeight = 1 + max(leftHeight, rightHeight)
        heightMap[node.val] = myHeight
        
        return myHeight