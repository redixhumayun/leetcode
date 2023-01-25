class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float("inf")
        self.min_values_list = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_value:
            self.min_value = val
            self.min_values_list.append(val)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min_values_list[-1]:
            self.min_values_list.pop()
            if len(self.min_values_list) > 0:
                self.min_value = self.min_values_list[-1]
            else:
                self.min_value = float("inf")
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_value
        

if __name__ == '__main__':
    # min_stack = MinStack()
    # min_stack.push(-2)
    # min_stack.push(0)
    # min_stack.push(-3)
    # print(min_stack.getMin())
    # min_stack.pop()
    # print(min_stack.top())
    # print(min_stack.getMin())
    
    min_stack = MinStack()
    min_stack.push(2147483646)
    min_stack.push(2147483646)
    min_stack.push(2147483647)
    print(min_stack.top())
    min_stack.pop()
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())
    min_stack.pop()
    min_stack.push(2147483647)
    print(min_stack.top())
    print(min_stack.getMin())
    min_stack.push(-2147483648)
    print(min_stack.top())
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()