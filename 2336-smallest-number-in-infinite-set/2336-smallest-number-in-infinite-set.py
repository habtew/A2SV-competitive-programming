class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set()

    def popSmallest(self) -> int:
        smallest = 1
        while smallest in self.nums:
            smallest += 1
        # Add the found integer to the popped elements set
        self.nums.add(smallest)
        # Return the smallest integer
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.nums:
            self.nums.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)