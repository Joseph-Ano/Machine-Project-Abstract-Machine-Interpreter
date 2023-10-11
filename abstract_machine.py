class abstract_machine:
  def __init__(self, states, language, instructions, memory, input, curState, curInputIdx):
    self.states = states
    self.language = language
    self.transitions = instructions
    self.memory = memory
    self.input = input
    self.curState = curState
    self.curInputIdx = curInputIdx

  def scan(self):
    pass