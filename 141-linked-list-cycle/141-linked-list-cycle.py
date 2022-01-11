# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        
        slow, fast = head, head.next
        
        while fast and fast.next and slow and fast != slow:
            fast = fast.next.next
            slow = slow.next
        
        if fast == slow and fast != None:
            return True
        else:
            return False