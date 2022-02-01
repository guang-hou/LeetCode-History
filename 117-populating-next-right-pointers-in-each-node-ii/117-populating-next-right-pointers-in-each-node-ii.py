"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        first = root
        while first:  # 遍历每一层
            dummyHead = Node(None)  # 为下一行创建一个虚拟头节点，相当于下一行所有节点链表的头结点(每一层都会创建)；
            tail = dummyHead  # 为下一行维护一个尾节点指针（初始化是虚拟节点）
            cur = first
            while cur:  # 遍历当前层的节点（假设当前层所有节点已经连接好）, 处理下一层节点
                if cur.left:  # 链接下一行的节点
                    tail.next = cur.left
                    tail = cur.left
                if cur.right:
                    tail.next = cur.right
                    tail = cur.right
                cur = cur.next  # cur同层移动到下一节点
            first = dummyHead.next  # 此处为换行操作，更新到下一行
        return root