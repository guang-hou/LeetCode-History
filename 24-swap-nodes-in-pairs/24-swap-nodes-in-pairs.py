# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        elif not head.next: return head
        
        dummy_head = ListNode(0, head)
        
        pre, cur, nxt = dummy_head, head, head.next
        
        while cur and nxt:
            cur.next = nxt.next
            nxt.next = cur
            pre.next = nxt
            
            pre = cur
            cur = cur.next
            if cur:
                nxt = cur.next
        
        return dummy_head.next