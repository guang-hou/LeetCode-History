# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        if length == 1:
            return True
        #elif length == 2 and head.val != head.next.val:
        #    return False
        
        pre, cur = None, head
        
        for _ in range(0, length // 2):
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
            
        left_start = pre
        
        if length % 2 == 1:
            right_start = cur.next
        else:
            right_start = cur
        
        while right_start:
            if right_start.val != left_start.val:
                return False
            else:
                right_start = right_start.next
                left_start = left_start.next
        return True
        
        