from memory_structs.stack import* 
from memory_structs.customqueue import* 

class Memory:
    def __init__(self):
        self.stackDict = {}
        self.queueDict = {}
        self.tapeDict = {}
        self.tape_2dDict = {}

    def write(self, name, input):
        if(self.stackDict.has_key(name)):
            self.stackDict[name].write(input)

        elif(self.queueDict.has_key(name)):
            self.stackDict[name].write(input)
        
        else:
            pass

    def read(self, name):
        if(self.stackDict.has_key(name)):
            return self.stackDict[name].read(input)

        elif(self.queueDict.has_key(name)):
            return self.stackDict[name].read(input)
        
        else:
            return 0
        
    def isEmpty(self, name):
        if(self.stackDict.has_key(name)):
            return self.stackDict[name].check()

        elif(self.queueDict.has_key(name)):
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

    
        