class Tape_One_D:
    def __init__(self, name):
        self.name = name
        self.tape = []
        self.curPtr = 0

    def write(self, input):
        self.tape[self.curPtr] = input

    def read(self, offset=0):
        if(self.curPtr == len(self.tape)-1 and offset == 1):
            self.tape.append("#")
        elif(self.curPtr == 0 and offset == -1):
            self.tape.insert(0, "#")
            self.curPtr+=1

        result = self.tape[self.curPtr + offset]
        self.curPtr += offset

        return result
    
    def isEmpty(self):
        if(len(self.tape) == 0):
            return True
        else:
            return False
    
    def peek(self, offset=0):
        if(self.curPtr == len(self.tape)-1 and offset == 1):
            return "#"
        elif(self.curPtr == 0 and offset == -1):
            return "#"
        else:
            return self.tape[self.curPtr + offset]