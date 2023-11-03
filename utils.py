from memory import*

def get_machine_design():
    print("Enter input:")
    part = "empty"
    data = []
    logic = []

    while True:
        user_input = input()

        if user_input == '':
            break
        elif user_input == ".DATA":
            part = ".DATA"
        elif user_input == ".LOGIC":
            part = ".LOGIC"
        elif part == ".DATA":
            data.append(user_input)
        elif part == ".LOGIC":
            logic.append(user_input)

    return data, logic

def app_get_machine_design(text):

    part = "empty"
    data = []
    logic = []

    for line in text:
        if line == '':
            pass
        elif line == ".DATA":
            part = ".DATA"
        elif line == ".LOGIC":
            part = ".LOGIC"
        elif part == ".DATA":
            data.append(line)
        elif part == ".LOGIC":
            logic.append(line)

    return data, logic

def parse_logic_input(logic):
    states = set()
    language = set()
    memory_language = {}
    instructions = []

    for line in logic:
        components = line.strip().split(" ")
        sourceState = components[0][:-1]

        if(components[2] == "RIGHT" or components[2] =="LEFT"):
            action = " ".join(components[1:3])
            symbolAndDest = components[3:]
        else:
            action = components[1] # may contain memory
            symbolAndDest = components[2:]

        memory = ""

        idx = action.find('(')

        if(idx != -1): # separates actions from the memory if present
            memory = action[idx+1:-1]
            action = action[:idx]

        states.add(sourceState)

        for entry in symbolAndDest:
            # print(entry)
            symbol = entry[1: entry.find(",")] # gets the symbol
            dest = entry[entry.find(",")+1: -1] if entry[-1] == ')' else entry[entry.find(",")+1: -2]# gets the destination state
            # print(dest)

            if(memory != ""): # if line uses memory, include symbol as part of language for memory
                memory_language.setdefault(memory, set()).add(symbol)
            else: # include symbol as part of language
                language.add(symbol)

            instructions.append((sourceState, action, memory, symbol, dest))

    return states, language, memory_language, instructions  

def parse_data_input(data, input):
    memory = Memory()
    memory.initialize(data)
    for key, _ in memory.tapeDict.items():
        memory.tapeDict[key].tape = [char for char in input]
        break

    return memory

def get_valid_instructions(instructions, curState, input, curInputIdx):
    valid_instructions = []
    action = ""

    for instruction in instructions:
        if curState == instruction[0]:
            action = instruction[1]
            break

    if(action == "WRITE" or action == "READ"):
         for instruction in instructions:
            if curState == instruction[0]:
                valid_instructions.append(instruction)
        
    else:
        if(curInputIdx < len(input) and curInputIdx >= 0):
            for instruction in instructions:
                if curState == instruction[0] and input[curInputIdx] == instruction[3]:
                    valid_instructions.append(instruction)
    
    return valid_instructions

def get_current_input_state(curIndex, user_input):
    result = ""
    if(curIndex < 0):
        result += ">" + user_input
    elif(curIndex >= len(user_input)):
        result+= user_input + ">"
    else:
        for i in range(len(user_input)):
            if(i == curIndex):
                result += ">"
            result += user_input[i]
    return result

def print_machine(machine):
    # print(f"States: {machine.states}") 
    # print(f"Language: {machine.language}") 
    # print(f"Instructions: {machine.instructions}")
    print(f"CurState: {machine.curState}")
    print(f"Memory:")
    machine.memory.print_contents()
    print("=============================")
    print(f"Action: {machine.action}")
    print(f"Input: {machine.input}")
    print(f"CurInputIdx: {machine.curInputIdx}")
    # print(f"NextInputIdx: {machine.nextInputIdx}")
    print(f"Machine stack: {len(machine.machine_stack)}")
    print(f"Valid instructions: {machine.valid_instructions}")