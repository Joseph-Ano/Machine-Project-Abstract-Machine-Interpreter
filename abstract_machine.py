class One_Way_Accepter:
  def __init__(self, states, language, transitions, input):
    self.states = states
    self.language = language
    self.transitions = transitions
    self.input = input
    self.curInputPtr = 0
    self.curState = states[0]

  def scan(self):
    pass