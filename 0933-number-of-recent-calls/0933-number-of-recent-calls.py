
class RecentCounter:

    def __init__(self):
        self.head = deque()

    def ping(self, t: int) -> int:
        self.head.append(t)
        while self.head[0] < t - 3000:
            self.head.popleft()
        return len(self.head)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)