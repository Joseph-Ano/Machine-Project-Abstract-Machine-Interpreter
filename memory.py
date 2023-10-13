from memory_structs.stack import* 
from memory_structs.customqueue import* 

class Memory:
    def __init__(self):
        self.stackDict = {}
        self.queueDict = {}
        self.tapeDict = {}
        self.tape_2dDict = {}

    def write(self, name, input):
        if(name in self.stackDict):
            self.stackDict[name].write(input)

        elif(name in self.queueDict):
            self.stackDict[name].write(input)
        
        else:
            pass

    def read(self, name):
        if(name in self.stackDict):
            return self.stackDict[name].read(input)

        elif(name in self.queueDict):
            return self.stackDict[name].read(input)
        
        else:
            return 0
        
    def isEmpty(self, name):
        if(name in self.stackDict):
            return self.stackDict[name].check()

        elif(name in self.queueDict):
            return self.stackDict[name].check()
        
        else:
            return 0
        
    def initialize(self, data):
        for line in data:
            temp = line.split(" ")
            type = temp[0]
            name = temp[1]

            if(type == "STACK"):
                self.stackDict.setdefault(name, Stack(name))
            elif(type == "Queue"):
                self.queueDict.setdefault(name, CustomQueue(name))

    def print_contents(self):
        for stack in self.stackDict.values():
            print(stack.stack)
            
        # print(self.stackDict.values())
        # print(self.queueDict.values())
        

    
        