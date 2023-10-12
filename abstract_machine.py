from utils import *

class abstract_machine:
  def __init__(self, states, language, instructions, memory, curState, action, input, curInputIdx):
    self.states = states
    self.language = language
    self.instructions = instructions
    self.memory = memory
    self.curState = curState
    self.action = action
    self.input = input
    self.curInputIdx = curInputIdx
    self.valid_instructions = []
    self.machine_stack = []

  def scan(self):
    for valid_instruction in self.valid_instructions:
      next_state = valid_instruction[4]
      next_action = ""

      # find the action of the next state
      for instruction in self.instructions:
        if next_state == instruction[0]:
          next_action = instruction[1]
          break
      
      nextInputIdx = self.curInputIdx + 1

      self.machine_stack.append(abstract_machine(
        self.states,
        self.language,
        self.instructions,
        valid_instruction[2],
        next_state,
        next_action,
        self.input,
        nextInputIdx,
      ))
      
      self.machine_stack[-1].valid_instructions = get_valid_instructions(self.instructions, 
                                                                        next_state, 
                                                                        self.input, 
                                                                        nextInputIdx)
    if(len(self.machine_stack) > 0):
      self.get_next_machine()
  
  def scan_right(self):
    pass

  def scan_left(self):
    pass

  def get_next_machine(self):
      next_machine = self.machine_stack.pop()

      self.memory = next_machine.memory
      self.curState = next_machine.curState
      self.action = next_machine.action
      self.curInputIdx = next_machine.curInputIdx
      self.valid_instructions = next_machine.valid_instructions
  
  def start(self):
    startingIdx = self.curInputIdx
    
    if(self.action == "SCAN RIGHT"):
      startingIdx+=1
    elif(self.action == "SCAN LEFT"):
      startingIdx-=1

    self.valid_instructions = get_valid_instructions(self.instructions, self.instructions[0][0], self.input, startingIdx)

  def step(self):
    if(self.action =="SCAN"):
      self.scan()
    elif(self.action == "SCAN RIGHT"):
      self.scan_right()
    elif(self.action == "SCAN LEFT"):
      self.scan_left()
    else:
      self.get_next_machine()

  def run(self):
    while True:
      self.step()

      if(self.curState == "accept" and self.curInputIdx == len(self.input)):
        print("Input is accepted")
        break

      elif(len(self.machine_stack) == 0 and len(self.valid_instructions) == 0):
        print("Input is rejected")
        break

# TO DO
# think of terminating condition

