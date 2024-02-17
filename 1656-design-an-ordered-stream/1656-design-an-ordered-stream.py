class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.list_string = [None] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list_string[idKey] = value
        result = []
        while self.ptr < len(self.list_string) and self.list_string[self.ptr] is not None:
            result.append(self.list_string[self.ptr])
            self.ptr += 1

        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)