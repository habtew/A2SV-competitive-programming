class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
        self.size = 1
        

    def visit(self, url: str) -> None:
        # add url to linked list
        self.curr.next = Node(url)
        self.curr = self.curr.next
        self.size += 1

    def back(self, steps: int) -> str:
        # access url back from ll
        # 4 - 2 + 1,, 2
        pos = max(0, self.size - steps - 1)
        self.size = pos + 1
        cur = self.head
        for i in range(pos):
            cur = cur.next
        self.curr = cur
        return self.curr.val

    def forward(self, steps: int) -> str:
        # access url forward
        while steps and self.curr.next:
            self.size += 1
            steps -= 1
            self.curr = self.curr.next
        
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)