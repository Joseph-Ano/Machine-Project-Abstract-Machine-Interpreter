class Tape_Two_D:
    def __init__(self, name):
        self.name = name
        self.tape = []
        self.rowPtr = 0
        self.colPtr = 0

    def write(self, input):
        self.tape[self.rowPtr][self.colPtr] = input

    def read(self, colOffset=0, rowOffset=0):
        if(self.colPtr+colOffset == len(self.tape[0])-1 and colOffset == 1):
            for row in self.tape:
                row.append("#")
        elif(self.rowPtr+rowOffset == len(self.tape)-1 and rowOffset == 1):
            temp = ['#' for char in self.tape[0]]
            self.tape.append(temp)

        self.rowPtr += rowOffset
        self.colPtr += colOffset
        result = self.tape[self.rowPtr][self.colPtr]

        return result
    
    def isEmpty(self):
        if(len(self.tape) == 0):
            return True
        else:
            return False
    
    def peek(self, colOffset=0, rowOffset=0):
        if(self.colPtr+colOffset < 0):
            return "FAIL"
        elif(self.rowPtr+rowOffset < 0):
            return "FAIL"
        else:
            return self.tape[self.rowPtr+rowOffset][self.colPtr+colOffset]