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
            return self.stackDict[name].read()

        elif(name in self.queueDict):
            return self.stackDict[name].read()
        
        else:
            return 0
        
    def isEmpty(self, name):
        if(name in self.stackDict):
            return self.stackDict[name].isEmpty()

        elif(name in self.queueDict):
            return self.queueDict[name].isEmpty()
        
        else:
            return 0
        
    def peek(self, name):
        if(name in self.stackDict):
            return self.stackDict[name].peek()

        elif(name in self.queueDict):
            return self.stackDict[name].peek()
        
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
            print(f"{stack.name}: {stack.stack}")

        for queue in self.queueDict.values():
            print(f"{queue.name}: {queue.queue}")

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

        
            
        # print(self.stackDict.values())
        # print(self.queueDict.values())
        

    
        