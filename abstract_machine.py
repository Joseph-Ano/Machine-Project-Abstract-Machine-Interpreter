from utils import*
from memory import*
import copy

class abstract_machine:
  def __init__(self, states, language, instructions, memory, curState, action, input, curInputIdx, offset=0, output=""):
    self.states = states
    self.language = language
    self.instructions = instructions
    self.memory = memory
    self.curState = curState
    self.action = action
    self.input = input
    self.curInputIdx = curInputIdx
    self.previousAction = ""
    self.offset = offset
    self.output = output
    self.machineType = getMachineType(instructions)
    self.valid_instructions = get_valid_instructions(self.instructions, 
                                                     self.curState, 
                                                     self.input, 
                                                     self.curInputIdx + self.offset)
    self.machine_stack = []

  def print_action(self):
    for valid_instruction in self.valid_instructions:
      next_state = valid_instruction[4]
      next_action = ""

      # find the action of the next state
      for instruction in self.instructions:
        if next_state == instruction[0]:
          next_action = instruction[1]
          break

      offset = 0
      if(next_action == "SCAN RIGHT"):
        offset+=1
      elif(next_action == "SCAN LEFT"):
        offset-=1

      new_output = self.output + valid_instruction[3]

      self.machine_stack.append(abstract_machine(
        self.states,
        self.language,
        self.instructions,
        self.memory,
        next_state,
        next_action,
        self.input,
        self.curInputIdx,
        offset,
        new_output
      ))

      self.machine_stack[-1].previousAction = self.action

    if(len(self.machine_stack) > 0):
      self.get_next_machine()

  def scan(self, direction=1):
    for valid_instruction in self.valid_instructions:
      next_state = valid_instruction[4]
      next_action = ""

      # find the action of the next state
      for instruction in self.instructions:
        if next_state == instruction[0]:
          next_action = instruction[1]
          break
      
      nextInputIdx = self.curInputIdx + direction
      
      offset = 0
      if(next_action == "SCAN RIGHT"):
        offset+=1
      elif(next_action == "SCAN LEFT"):
        offset-=1

      self.machine_stack.append(abstract_machine(
        self.states,
        self.language,
        self.instructions,
        self.memory,
        next_state,
        next_action,
        self.input,
        nextInputIdx,
        offset,
        self.output
      ))
      
      self.machine_stack[-1].previousAction = self.action

    if(len(self.machine_stack) > 0):
      self.get_next_machine()
  
  def scan_right(self):
    self.scan(1)

  def scan_left(self):
    self.scan(-1)

  def write(self):
    for valid_instruction in self.valid_instructions:
      next_state = valid_instruction[4]
      next_action = ""

      # find the action of the next state
      for instruction in self.instructions:
        if next_state == instruction[0]:
          next_action = instruction[1]
          break

      offset = 0
      if(next_action == "SCAN RIGHT"):
        offset+=1
      elif(next_action == "SCAN LEFT"):
        offset-=1

      self.machine_stack.append(abstract_machine(
        self.states,
        self.language,
        self.instructions,
        copy.deepcopy(self.memory),
        next_state,
        next_action,
        self.input,
        self.curInputIdx,
        offset,
        self.output
      ))

      self.machine_stack[-1].previousAction = self.action
      writeResult = self.machine_stack[-1].memory.write(valid_instruction[2], valid_instruction[3])

      if(writeResult == "FAILED"):
         self.machine_stack.pop()

    if(len(self.machine_stack) > 0):
      self.get_next_machine()
    else:
      self.valid_instructions = []

  def read(self):
    for valid_instruction in self.valid_instructions:
      memoryName = valid_instruction[2]
      symbolToBeRead = valid_instruction[3]

      if(not self.memory.isEmpty(memoryName) and symbolToBeRead == self.memory.peek(memoryName)):
        next_state = valid_instruction[4]
        next_action = ""

        # find the action of the next state
        for instruction in self.instructions:
          if next_state == instruction[0]:
            next_action = instruction[1]
            break

        offset = 0
        if(next_action == "SCAN RIGHT"):
          offset+=1
        elif(next_action == "SCAN LEFT"):
          offset-=1

        self.machine_stack.append(abstract_machine(
          self.states,
          self.language,
          self.instructions,
          copy.deepcopy(self.memory),
          next_state,
          next_action,
          self.input,
          self.curInputIdx,
          offset,
          self.output
        ))

        self.machine_stack[-1].previousAction = self.action
        self.machine_stack[-1].memory.read(memoryName)

    if(len(self.machine_stack) > 0):
      self.get_next_machine()
    else:
      self.valid_instructions = []

  def right(self, colOffset=1, rowOffset=0):
    inputTape = ""

    for valid_instruction in self.valid_instructions:
      tempMemory = copy.deepcopy(self.memory)
      memoryName = valid_instruction[2]
      symbolToBeRead = valid_instruction[3][0]
      symbolToReplace = valid_instruction[3][2]

      for key, _ in tempMemory.tapeDict.items():
        if memoryName == key:
          inputTape = key
        break

      for key, _ in tempMemory.tape_2dDict.items():
        if memoryName == key:
          inputTape = key
        break

      print(symbolToBeRead)
      print(tempMemory.peek(memoryName, colOffset, rowOffset))
      if(symbolToBeRead == tempMemory.peek(memoryName, colOffset, rowOffset)):
        next_state = valid_instruction[4]
        next_action = ""

        # find the action of the next state
        for instruction in self.instructions:
          if next_state == instruction[0]:
            next_action = instruction[1]
            break

        offset = 0
        if(next_action == "SCAN RIGHT"):
          offset+=1
        elif(next_action == "SCAN LEFT"):
          offset-=1

        self.machine_stack.append(abstract_machine(
          self.states,
          self.language,
          self.instructions,
          tempMemory,
          next_state,
          next_action,
          self.input,
          self.curInputIdx,
          offset
        ))

        self.machine_stack[-1].previousAction = self.action
        self.machine_stack[-1].memory.read(memoryName, colOffset, rowOffset)
        writeResult = self.machine_stack[-1].memory.write(memoryName, symbolToReplace)

        if(inputTape != ""):
          if(inputTape in self.machine_stack[-1].memory.tapeDict):
            tapeHead = self.machine_stack[-1].memory.tapeDict[memoryName].curPtr
            self.machine_stack[-1].output = "".join(self.machine_stack[-1].memory.tapeDict[memoryName].tape[tapeHead+1:])
          else:
            tapeHeadRow = self.machine_stack[-1].memory.tape_2dDict[memoryName].rowPtr
            tapeHeadCol = self.machine_stack[-1].memory.tape_2dDict[memoryName].colPtr
            self.machine_stack[-1].output = "".join(self.machine_stack[-1].memory.tape_2dDict[memoryName].tape[tapeHeadRow][tapeHeadCol+1:])

        if(writeResult == "FAILED"):
          self.machine_stack.pop()

    if(len(self.machine_stack) > 0):
      self.get_next_machine()
    else:
      self.valid_instructions = []

  def left(self):
    self.right(-1)

  def up(self):
    self.right(0, -1)

  def down(self):
    self.right(0, 1)

  def get_next_machine(self):
      next_machine = self.machine_stack.pop()

      self.memory = next_machine.memory
      self.curState = next_machine.curState
      self.action = next_machine.action
      self.input = next_machine.input
      self.curInputIdx = next_machine.curInputIdx
      self.previousAction = next_machine.previousAction
      self.offset = next_machine.offset
      self.valid_instructions = next_machine.valid_instructions
      self.output = next_machine.output
 
  def step(self):
    if(self.action =="PRINT"):
      self.print_action()
    elif(self.action =="SCAN"):
      self.scan()
    elif(self.action == "SCAN RIGHT"):
      self.scan_right()
    elif(self.action == "SCAN LEFT"):
      self.scan_left()
    elif(self.action == "WRITE"):
      self.write()
    elif(self.action == "READ"):
      self.read()
    elif(self.action == "RIGHT"):
      self.right()
    elif(self.action == "LEFT"):
      self.left()
    elif(self.action == "UP"):
      self.up()
    elif(self.action == "DOWN"):
      self.down()
    else:
      self.get_next_machine()

  def run(self):
    while True:
      self.step()

      if(self.curState == "accept"):
        break

      elif(len(self.machine_stack) == 0 and len(self.valid_instructions) == 0):
        break

