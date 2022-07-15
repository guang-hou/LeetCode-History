class MyQueue:

    def __init__(self):
        self.pushStack = []
        self.popStack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.pushStack.append(x)
        self.size += 1
        
    def pop(self) -> int:
        if self.empty():
            return None
        
        if not self.popStack:
            self.moveElements()
        
        self.size -= 1
        return self.popStack.pop()
        
            
    def peek(self) -> int:
        if self.empty():
            return None
        
        if not self.popStack:
            self.moveElements()
        
        return self.popStack[-1]

    def empty(self) -> bool:
        return self.size == 0
    
    def moveElements(self):
        while self.pushStack:
            self.popStack.append(self.pushStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()