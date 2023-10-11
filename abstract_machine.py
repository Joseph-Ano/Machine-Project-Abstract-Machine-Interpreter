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
    self.machine_stack = []
    self.valid_instructions = get_valid_instructions(instructions, curState, input, curInputIdx)

  def scan(self):
    if(self.curInputIdx < len(self.input)-1):
      for valid_instruction in self.valid_instructions:
        next_state = valid_instruction[4]
        next_action = ""

        # to find the action of the next state
        for instruction in self.instructions:
          if next_state == instruction[0]:
            next_action = instruction[1]
            break

        self.machine_stack.append(abstract_machine(
          self.states,
          self.language,
          self.instructions,
          valid_instruction[2],
          next_state,
          next_action,
          self.input,
          self.curInputIdx + 1
        ))
  
    future_machine = self.machine_stack.pop()

    self.memory = future_machine.memory
    self.curState = future_machine.curState
    self.action = future_machine.action
    self.curInputIdx = future_machine.curInputIdx
    self.valid_instructions = future_machine.valid_instructions

  def run_machine(self):
    if(self.action =="SCAN"):
      self.scan()
    else:
      self.machine_stack.pop()
      # self.scan()
      # print(self)

