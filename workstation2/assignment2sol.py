class stack:
    def __init__(self) -> None:
        self.item = []

    def push(self, val: str) -> None:
        self.item.append(val)

    def pop(self) -> str:
        if self.empty():
            raise KeyError("You cannot raise an empty stack.")
        return self.item.pop()
    
    def empty(self) -> int:
        