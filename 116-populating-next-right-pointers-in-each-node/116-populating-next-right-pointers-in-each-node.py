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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        
        first = root
        
        while first:
            cur = first
            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.right and cur.next: cur.right.next = cur.next.left
                cur = cur.next
            first = first.left
        
        return root