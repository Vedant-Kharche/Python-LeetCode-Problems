class MinStack:
    def __init__(self):
        # Normal stack to store values
        self.stack = []
        # Auxiliary stack to store the minimum value at each level
        self.minStack = []

    def push(self, val: int) -> None:
        # Push the value onto the normal stack
        self.stack.append(val)

        # Determine the new minimum:
        # - If minStack has values, compare current val with the last minimum
        # - Otherwise, the value itself is the minimum
        val = min(val, self.minStack[-1] if self.minStack else val)

        # Push the new minimum onto minStack
        self.minStack.append(val)

    def pop(self) -> None:
        # Pop from both stacks because they grow and shrink together
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The top of minStack is always the current minimum
        return self.minStack[-1]
