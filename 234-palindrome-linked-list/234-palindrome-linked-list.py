# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        length = 0
        
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        cur = head
        for _ in range(1, length // 2 + 1):
            stack.append(cur.val)
            cur = cur.next
        
        if length % 2 == 0:
            right_start = length // 2 + 1
        else:
            right_start = length // 2 + 2
            cur = cur.next
        
        while stack:
            if stack[-1] != cur.val:
                return False
            else:
                stack.pop()
                cur = cur.next
        
        return True
        
        