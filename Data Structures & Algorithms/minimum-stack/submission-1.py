class MinStack:

    def __init__(self):
        self.list = []
        self.min = []
        

    def push(self, val: int) -> None:
        if len(self.list) == 0:
            self.list.append(val)
            self.min.append(val)
        else:
            self.list.append(val)
            if self.list[-1] <= self.min[-1]:
                self.min.append(val)
        return None
        

    def pop(self) -> None:
        if self.list[-1] == self.min[-1]:
            self.list.pop()
            self.min.pop()
        else:
            self.list.pop()
        return None

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int: 
        return self.min[-1]
        
