class MyStack:

    def __init__(self):
        self.lastElement = deque()
        self.prevElements = deque()
        self.size = 0
        

    def push(self, x: int) -> None:
        if self.lastElement:
            self.prevElements.append(self.lastElement.popleft())
            
        self.lastElement.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return None
        
        element = self.lastElement.popleft()
        
        self.rebalance()
        
        self.size -= 1
        return element

    def top(self) -> int:
        if self.empty():
            return None
        
        return self.lastElement[0]

    def empty(self) -> bool:
        return self.size == 0
        
    def rebalance(self):
        while self.prevElements:
            self.lastElement.append(self.prevElements.popleft())
        while len(self.lastElement) > 1:
            self.prevElements.append(self.lastElement.popleft())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()