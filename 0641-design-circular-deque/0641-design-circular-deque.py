class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.stack = deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if len(self.stack) == self.size:
            return False
        else:
            self.stack.appendleft(value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.stack) == self.size:
            return False
        else:
            self.stack.append(value)
            return True

    def deleteFront(self) -> bool:
        if len(self.stack) == 0:
            return False
        else:
            self.stack.popleft()
            return True

    def deleteLast(self) -> bool:
        if len(self.stack):
            self.stack.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.stack:
            return self.stack[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.stack

    def isFull(self) -> bool:
        return len(self.stack) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()