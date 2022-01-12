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
        data = []
        cur = head
        while cur:
            data.append(cur.val)
            cur = cur.next
            
        cur = head
        left, right = 1, len(data) - 1
        while left <= right:
            right_node = ListNode(data[right])
            cur.next = right_node
            right -= 1
            cur = cur.next
            
            if left <= right:
                left_node = ListNode(data[left])
                cur.next = left_node
                cur = cur.next
                left += 1
        
            
        
        
            
        
        