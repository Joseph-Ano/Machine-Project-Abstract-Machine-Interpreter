def get_machine_design():
    print("Enter input:")
    part = "empty"
    data = []
    logic = []

    while True:
        user_input = input()

        # 👇️ if user pressed Enter without a value, break out of loop
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

def parse_logic_input(logic):
    states = set()
    language = set()
    memory_language = {}
    instructions = []

    for line in logic:
        components = line.split(" ")
        symbolAndDest = components[2:]

        for entry in symbolAndDest:
            sourceState = components[0][:-1]
            action = components[1] # may contain memory
            memory = ""

            idx = action.find('(')

            if(idx != -1): # separates actions from the memory if present
                memory = action[idx+1:-1]
                action = action[:idx]

            symbol = entry[1: entry.find(",")] # gets the symbol
            dest = entry[entry.find(",")+1: -1] if entry[-1] == ')' else entry[entry.find(",")+1: -2]# gets the destination state

            states.add(sourceState)

            if(memory != ""): # if line uses memory, includ symbol as part of language for memory
                memory_language.setdefault(memory, set()).add(symbol)
            else: # include symbol as part of language
                language.add(symbol)

            instructions.append((sourceState, action, memory, symbol, dest))
            
    # print(memory_language)
    return states, language, memory_language, instructions  

def get_valid_instructions(instructions, curState, input, curInputIdx):
    valid_instructions = []
    for instruction in instructions:
        if curState == instruction[0] and input[curInputIdx] == instruction[3]:
            valid_instructions.append(instruction)
    
    return valid_instructions

def print_machine(machine):
    # print(f"States: {machine.states}") 
    # print(f"Language: {machine.language}") 
    print(f"Instructions: {machine.instructions}")
    # print(f"Memory: {machine.memory}")
    print(f"CurState: {machine.curState}")
    print(f"Action: {machine.action}")
    print(f"Input: {machine.input}")
    print(f"CurInputIdx: {machine.curInputIdx}")
    # print(f"Machine stack: {len(machine.machine_stack)}")
    print(f"Valid instructions: {machine.valid_instructions}")















# def find_logic_section(inputs: list):
#     for i in range(len(inputs)):
#         if(inputs[i].strip() == ".LOGIC"):
#             return i
#     return -1


# def find_data_section(inputs: list):
#     for i in range(len(inputs)):
#         if(inputs[i].strip() == ".DATA"):
#             return i
#     return -1