# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode(0, head)
        
        pre, cur = dummy_head, head
        
        while cur and cur.next:
            post = cur.next
            
            cur.next = post.next
            post.next = cur
            pre.next = post
            
            pre = cur
            cur = pre.next
        
        return dummy_head.next