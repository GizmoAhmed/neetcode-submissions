class MinStack:

    def __init__(self):
        self.stack = []
        self.pre = []
        

    def push(self, val: int) -> None:
        print("Before Push: ", self.stack)

        self.stack.append(val)
        
        if len(self.pre) == 0 or self.pre[-1] >= val:
            self.pre.append(val)

        print("After Push: ", self.stack)
        

    def pop(self) -> None:
        print("Before Pop: ", self.stack)
        pop_me = self.stack.pop()
        print("After Pop: ", self.stack)

        if pop_me == self.pre[-1]:
            self.pre.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.pre[-1]
        
