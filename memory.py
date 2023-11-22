from memory_structs.stack import* 
from memory_structs.customqueue import* 
from memory_structs.tape_oned import* 
from memory_structs.tape_twod import* 
from collections import OrderedDict

class Memory:
    def __init__(self):
        self.stackDict = {}
        self.queueDict = {}
        self.tapeDict = OrderedDict()
        self.tape_2dDict = OrderedDict()

    def write(self, name, input):
        if(name in self.stackDict):
            self.stackDict[name].write(input)
        elif(name in self.queueDict):
            self.queueDict[name].write(input)
        elif(name in self.tapeDict):
            self.tapeDict[name].write(input)
        elif(name in self.tape_2dDict):
            self.tape_2dDict[name].write(input)
        else:
            return "FAILED"
        
        return "PASSED"

    def read(self, name, colOffset=0, rowOffset=0):
        if(colOffset == 0 and rowOffset == 0):
            if(name in self.stackDict):
                self.stackDict[name].read()
            elif(name in self.queueDict):
                self.queueDict[name].read()
            
        elif(colOffset != 0 and rowOffset == 0):
            if(name in self.tapeDict):
                self.tapeDict[name].read(colOffset)
            elif(name in self.tape_2dDict):
                self.tape_2dDict[name].read(colOffset)

        else:
            if(name in self.tape_2dDict):
                self.tape_2dDict[name].read(colOffset, rowOffset)
        
    def peek(self, name, colOffset=0, rowOffset=0):
        if(colOffset == 0 and rowOffset == 0):
            if(name in self.stackDict):
                return self.stackDict[name].peek()
            elif(name in self.queueDict):
                return self.queueDict[name].peek()
            else:
                return "FAILED"
            
        elif(colOffset != 0 and rowOffset == 0):
            if(name in self.tapeDict):
                return self.tapeDict[name].peek(colOffset)
            elif(name in self.tape_2dDict):
                return self.tape_2dDict[name].peek(colOffset)
            else:
                return "FAILED"
            
        else:
            if(name in self.tape_2dDict):
                return self.tape_2dDict[name].peek(colOffset, rowOffset)
            else:
                return "FAILED"
        
    def isEmpty(self, name):
        if(name in self.stackDict):
            return self.stackDict[name].isEmpty()
        elif(name in self.queueDict):
            return self.queueDict[name].isEmpty()
        else:
            return True
        
    def initialize(self, data):
        for line in data:
            temp = line.split(" ")
            type = temp[0]
            name = temp[1]

            if(type == "STACK"):
                self.stackDict.setdefault(name, Stack(name))
            elif(type == "QUEUE"):
                self.queueDict.setdefault(name, CustomQueue(name))
            elif(type == "TAPE"):
                self.tapeDict.setdefault(name, Tape_One_D(name))
            elif(type == "2D_TAPE"):
                self.tape_2dDict.setdefault(name, Tape_Two_D(name))

    def print_stack_contents(self):
        result = ""
        for stack in self.stackDict.values():
            result += f"{stack.name}: {stack.stack}\n"
        
        return result
    
    def print_queue_contents(self):
        result = ""
        for queue in self.queueDict.values():
            result += f"{queue.name}: {queue.queue}\n"
        
        return result
    
    def print_tape_contents(self):
        result = ""
        for tape in self.tapeDict.values():
            result += f"{tape.name}: [ "
            for i in range(len(tape.tape)):
                if(i == tape.curPtr):
                    result += ">"
                result += f"{tape.tape[i]} "
            result += "]\n"

        return result

    def print_tape_2d_contents(self):
        result = ""
        for tape in self.tape_2dDict.values():
            result += f"{tape.name}:\n [ "
            for i in range(len(tape.tape)):
                for j in range(len(tape.tape[0])):
                    if(i == tape.rowPtr and j == tape.colPtr):
                        result += ">"
                    result += f"{tape.tape[i][j]} "
                if(i < len(tape.tape) - 1):
                    result += "\n"
            result += "]\n"

        return result
       
        

    
        