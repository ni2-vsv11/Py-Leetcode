class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        

    def push(self, x: int) -> None:
        while len(self.stk1)>0:
            self.stk2.append(self.stk1.pop())
        self.stk1.append(x)
        while len(self.stk2)>0:
            self.stk1.append(self.stk2.pop())
        
    def pop(self) -> int:
        x = self.stk1[-1]
        self.stk1.pop()
        return x

    def peek(self) -> int:
        return self.stk1[-1]

    def empty(self) -> bool:
        return len(self.stk1)==0
        
 