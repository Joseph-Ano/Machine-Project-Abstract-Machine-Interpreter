class Tape_One_D:
    def __init__(self, name):
        self.name = name
        self.tape = []
        self.curPtr = 0

    def write(self, input):
        self.tape[self.curPtr] = input

    def read(self, offset=0):
        result = self.tape[self.curPtr + offset]
        self.curPtr += offset

        return result
    
    def isEmpty(self):
        if(len(self.tape) == 0):
            return True
        else:
            return False
    
    def peek(self, offset=0):
        return self.tape[self.curPtr + offset]