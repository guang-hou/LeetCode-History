# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return None
        
        slow, fast = head, head
        
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None  # cut off the firt half with the rest
        
        prev = None
        cur = slow
        while cur:
            post = cur.next
            cur.next = prev
            prev = cur
            cur = post
        
        right = prev
        left = head
        
        while left:
            if left.next:
                left_post = left.next
                right_post = right.next
                left.next = right
                right.next = left_post
                left = left_post
                right = right_post
            else:
                left.next = right
                break
        
            
        
        
            
        
        