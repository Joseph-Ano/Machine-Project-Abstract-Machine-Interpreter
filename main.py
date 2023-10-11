from utils import*
from abstract_machine import*


def main():
    data, logic = get_machine_design()
    # print(data)
    # print(logic)

    states, language, memory_language, instructions = parse_logic_input(logic)
    # valid_instructions = get_valid_instructions(instructions, 'E', '#1', 1)
    # print(valid_instructions)

    input = "00000101010100101"
    idx = 0
    memory = "temp"
    machine = abstract_machine(states, 
                               language, 
                               instructions, 
                               memory, 
                               instructions[0][0], 
                               instructions[0][1], 
                               input, 
                               idx)
    machine.start()
    # machine.machine_stack.append(machine)
    # machine.step()
    # print_machine(machine)
    # print("\n")
    # machine.tep()
    # print_machine(machine)
    machine.run()

main()



