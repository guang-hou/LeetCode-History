# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        
        dummy_head = ListNode(0, head)
        cur_node = dummy_head  # this varialbe records the latest node whose valu != val 
        
        while cur_node.next: # this equals to: cur_node.next != None
            next_node = cur_node.next
            if next_node.val == val:   # compare this node value with val
                cur_node.next = next_node.next
            else:
                cur_node = cur_node.next
        
        return dummy_head.next
                
            
        