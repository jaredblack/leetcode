class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not len(self._min_stack) or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        ret = self._stack.pop()
        if ret == self._min_stack[-1]:
            self._min_stack.pop()
        return ret
        
    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]

minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
