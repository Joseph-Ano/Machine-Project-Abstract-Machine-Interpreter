from memory_structs.stack import* 
from memory_structs.customqueue import* 
from memory_structs.tape_oned import* 
from collections import OrderedDict

class Memory:
    def __init__(self):
        self.stackDict = {}
        self.queueDict = {}
        self.tapeDict = OrderedDict()
        self.tape_2dDict = OrderedDict()

    def write(self, name, input, isTape=False):
        if(isTape):
            if(name in self.tapeDict):
                self.tapeDict[name].write(input)
            else:
                return "FAILED"
        else:
            if(name in self.stackDict):
                self.stackDict[name].write(input)
            elif(name in self.queueDict):
                self.queueDict[name].write(input)
            else:
                return "FAILED"
        return "PASSED"

    def read(self, name, offset=0):
        if(offset == 0):
            if(name in self.stackDict):
                self.stackDict[name].read()
            elif(name in self.queueDict):
                self.queueDict[name].read()
            
        else:
            if(name in self.tapeDict):
                self.tapeDict[name].read(offset)
           
        
    def peek(self, name, offset=0):
        if(offset == 0):
            if(name in self.stackDict):
                return self.stackDict[name].peek()
            elif(name in self.queueDict):
                return self.queueDict[name].peek()
            else:
                return "FAILED"
            
        else:
            if(name in self.tapeDict):
                return self.tapeDict[name].peek(offset)
            else:
                return "FAILED"
        
    def isEmpty(self, name):
        if(name in self.stackDict):
            return self.stackDict[name].isEmpty()

        elif(name in self.queueDict):
            return self.queueDict[name].isEmpty()
        
        elif(name in self.tapeDict):
            return self.tapeDict[name].isEmpty()
        
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

    def print_contents(self):
        for stack in self.stackDict.values():
            print(f"{stack.name}: {stack.stack}")

        for queue in self.queueDict.values():
            print(f"{queue.name}: {queue.queue}")

        for tape in self.tapeDict.values():
            print(f"{tape.name}: {tape.tape} - Current index: {tape.curPtr}")

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
            result += "[ "
            for i in range(len(tape.tape)):
                if(i == tape.curPtr):
                    result += ">"
                result += f"{tape.tape[i]} "
            result += "]\n"

        return result

        # print(self.stackDict.values())
       
        

    
        