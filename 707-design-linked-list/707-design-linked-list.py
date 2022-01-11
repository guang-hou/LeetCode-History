class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        if not self.head:
            self.head = new_head
        else:
            new_head.next = self.head
            self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        if not self.head:
            self.head = new_tail
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        
        elif index == self.length:
            self.addAtTail(val)
        
        elif index > 0 and index < self.length:
            cur = self.head
            while index > 1:
                cur = cur.next
                index -= 1
            temp = cur.next
            cur.next = Node(val, temp)
            self.length += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
                self.length -= 1
        
        elif index > 0 and index < self.length:
            cur = self.head
            while index > 1:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
            self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)