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

      if(nextInputIdx < len(self.input)):
        self.machine_stack[-1].valid_instructions = get_valid_instructions(self.instructions, 
                                                                           next_state, 
                                                                           self.input, 
                                                                          nextInputIdx)
  
    self.get_future_machine()
  
  def scan_right(self):
    self.scan()

  def get_future_machine(self):
      future_machine = self.machine_stack.pop()

      self.memory = future_machine.memory
      self.curState = future_machine.curState
      self.action = future_machine.action
      self.curInputIdx = future_machine.curInputIdx
      self.valid_instructions = future_machine.valid_instructions
  
  def start(self):
    startingIdx = self.curInputIdx

    if(self.action == "SCAN RIGHT"):
      startingIdx = self.curInputIdx + 1

    self.valid_instructions = get_valid_instructions(self.instructions, self.instructions[0][0], self.input, startingIdx)

  def step(self):
    if(self.action =="SCAN"):
      self.scan()
    elif(self.action == "SCAN RIGHT"):
      self.scan_right()
    # else:
    #   self.get_future_machine()

  def run(self):
    while True:
      self.step()

      if(self.curState == "accept"):
        print("Input is accepted")
        break
      elif(len(self.machine_stack) == 0 and len(self.valid_instructions) == 0):
        print("Input is rejected")
        break

# TO DO
# THINK OF BETTER STACK
# FIX INPUT START AND END

