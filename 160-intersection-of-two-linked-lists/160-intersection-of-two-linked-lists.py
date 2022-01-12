# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        
        cur1 = headA
        while cur1:
            stack1.append(cur1)
            cur1 = cur1.next
        
        cur2 = headB
        while cur2:
            stack2.append(cur2)
            cur2 = cur2.next
        
        pre = None
        while stack1 and stack2:
            if stack1[-1] == stack2[-1]:
                pre = stack1.pop()
                stack2.pop()
            else:
                return pre
        
        return pre