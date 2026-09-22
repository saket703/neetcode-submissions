class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimum=[]
    def push(self, val: int) -> None:
        self.minimum.append(min(self.minimum[-1] if len(self.minimum)>0 else val,val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
    
        return self.minimum[-1]
