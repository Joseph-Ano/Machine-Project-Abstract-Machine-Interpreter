from utils import*
from memory import*
import copy

class abstract_machine:
  def __init__(self, states, language, instructions, memory, curState, action, input, curInputIdx, offset=0):
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
    self.valid_instructions = get_valid_instructions(self.instructions, 
                                                     self.curState, 
                                                     self.input, 
                                                     self.curInputIdx + self.offset)
    self.machine_stack = []

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
        offset
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
        offset
      ))

      self.machine_stack[-1].previousAction = self.action
      self.machine_stack[-1].memory.write(valid_instruction[2], valid_instruction[3])

    if(len(self.machine_stack) > 0):
      self.get_next_machine()

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
          offset
        ))

        self.machine_stack[-1].previousAction = self.action
        self.machine_stack[-1].memory.read(memoryName)

    if(len(self.machine_stack) > 0):
      self.get_next_machine()
    else:
      self.valid_instructions = []

  def right(self, tapeOffset=1):
    isInputTape = False

    for valid_instruction in self.valid_instructions:
      tempMemory = copy.deepcopy(self.memory)
      memoryName = valid_instruction[2]
      symbolToBeRead = valid_instruction[3][0]
      symbolToReplace = valid_instruction[3][2]

      for key, _ in tempMemory.tapeDict.items():
        if memoryName == key:
          isInputTape = True
          tempMemory.tapeDict[key].curPtr = self.curInputIdx
        break

      if(not tempMemory.isEmpty(memoryName) and symbolToBeRead == tempMemory.peek(memoryName, tapeOffset)):
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

        if(tempMemory.tapeDict[memoryName].curPtr + tapeOffset <= len(tempMemory.tapeDict[memoryName].tape)-1 and 
           tempMemory.tapeDict[memoryName].curPtr + tapeOffset >= 0):  
          tempInput = self.input
          tempInputIdx = self.curInputIdx

          if(isInputTape):
            tempInputIdx = tempInputIdx + tapeOffset
            tempInput = self.input[:tempInputIdx] + symbolToReplace + self.input[tempInputIdx + 1:]

          self.machine_stack.append(abstract_machine(
            self.states,
            self.language,
            self.instructions,
            tempMemory,
            next_state,
            next_action,
            tempInput,
            tempInputIdx,
            offset
          ))

          self.machine_stack[-1].previousAction = self.action
          self.machine_stack[-1].memory.read(memoryName, tapeOffset)
          self.machine_stack[-1].memory.write(memoryName, symbolToReplace)

    if(len(self.machine_stack) > 0):
      self.get_next_machine()
    else:
      self.valid_instructions = []

  def left(self):
    self.right(-1)

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
  
  def start(self):
    offset = 0
    
    if(self.action == "SCAN RIGHT"):
      offset+=1
    elif(self.action == "SCAN LEFT"):
      offset-=1

    self.valid_instructions = get_valid_instructions(self.instructions, 
                                                      self.curState, 
                                                      self.input, 
                                                      self.curInputIdx + offset)

  def step(self):
    if(self.action =="SCAN"):
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
    else:
      self.get_next_machine()

  def run(self):
    # print_machine(self)
    # print("\n")
    
    while True:
      self.step()
      # print_machine(self)
      # print("\n")

      if(self.curState == "accept" and self.curInputIdx == len(self.input)):
        # print("Input is accepted")
        break

      elif(self.curState == "accept" and (self.curInputIdx == len(self.input)-1 and self.previousAction == "SCAN RIGHT")):
        # print("Input is accepted")
        break

      elif(self.curState == "accept" and (self.curInputIdx == 0 and self.previousAction == "SCAN LEFT")):
        # print("Input is accepted")
        break

      elif(len(self.machine_stack) == 0 and len(self.valid_instructions) == 0 ):
        # print("Input is rejected")
        break

