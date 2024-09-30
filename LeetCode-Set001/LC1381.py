class CustomStack:

    def __init__(self, maxSize: int):
        self.List = []
        self.maxSize = maxSize
        self.Size = 0


    def push(self, x: int) -> None:
        if self.Size < self.maxSize:
            self.List.append(x)
            self.Size += 1

    def pop(self) -> int:
        if self.Size > 0:
            self.Size -= 1
            return self.List.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k <= self.Size:
            for i in range(k):
                self.List[i] += val
        else:
            for i in range(self.Size):
                self.List[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)