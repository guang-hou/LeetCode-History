"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        dq = deque([root])
        
        while dq:
            n = len(dq)
            
            for i in range(n):
                cur = dq.popleft()
                if i < n - 1: cur.next = dq[0]
            
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
         
        return root