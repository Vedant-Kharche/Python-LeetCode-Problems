class MinStack:
    def __init__(self):
        # Main stack to store all values
        self.stack = []
        # Auxiliary stack that tracks the minimum value at each point in time
        self.minStack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)

        # Compute the new minimum:
        # - If minStack has items, compare the current value with the last stored minimum
        # - If minStack is empty, current value itself is the minimum
        newMin = val if not self.minStack else min(val, self.minStack[-1])

        # Push the computed minimum to minStack
        self.minStack.append(newMin)

    def pop(self) -> None:
        # Pop the top element from both stacks
        # (Each position in minStack corresponds to the same position in stack)
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top value of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top value of minStack (the current minimum)
        return self.minStack[-1]
