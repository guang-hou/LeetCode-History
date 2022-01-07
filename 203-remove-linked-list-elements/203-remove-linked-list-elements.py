# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        
        dummy_head = ListNode(0, head)
        cur_node = dummy_head
        
        while cur_node and cur_node.next:
            next_node = cur_node.next
            if next_node.val == val:
                cur_node.next = next_node.next
            else:
                cur_node = cur_node.next
        
        return dummy_head.next
                
            
        