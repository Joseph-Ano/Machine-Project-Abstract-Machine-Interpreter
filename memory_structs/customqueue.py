class CustomQueue:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def write(self, input):
        self.queue.append(input)

    def read(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        if(len(self.queue) == 0):
            return True
        else:
            return False
        
    def peek(self):
        return self.queue[0]
        