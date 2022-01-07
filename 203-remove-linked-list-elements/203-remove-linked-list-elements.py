# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        
        dummy_head = ListNode(0, head)
        previous = dummy_head
        cur_node = head
        
        while cur_node:
            if cur_node.val == val:
                previous.next = cur_node.next
                cur_node = cur_node.next
            else:
                previous = cur_node
                cur_node = cur_node.next
            
        return dummy_head.next
                
            
        