class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return not self.stack
    def size(self):
        return len(self.stack)
    def __str__(self):
        return str(self.stack)