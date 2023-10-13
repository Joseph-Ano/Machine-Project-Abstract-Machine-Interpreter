class CustomQueue:
    def __init__(self, name):
        self.name = name
        self.queue = []
        self.curPtr = 0

    def write(self, input):
        self.queue.append(input)

    def read(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        if(len(self.queue) == 0):
            return True
        else:
            return False
        