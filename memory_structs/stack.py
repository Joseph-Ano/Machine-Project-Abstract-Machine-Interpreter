class Stack:
    def __init__(self, name):
        self.name = name
        self.stack = []

    def write(self, input):
        self.stack.append(input)

    def read(self):
        return self.stack.pop()
    
    def isEmpty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False
    
    def peek(self):
        return self.stack[-1]
    