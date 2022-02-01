"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return None
        
        res = []
        dq = deque([root])
        
        while dq:
            n = len(dq)
            tmp = []
            
            for _ in range(n):
                cur = dq.popleft()
                tmp.append(cur.val)
                if cur.children:
                    for node in cur.children:
                        dq.append(node)
                        
            res.append(tmp)
        
        return res
                    