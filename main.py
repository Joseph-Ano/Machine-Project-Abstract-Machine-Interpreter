from utils import*
from abstract_machine import*


def main():
    data, logic = get_machine_design()
    # print(data)
    # print(logic)

    states, language, memory_language, instructions = parse_logic_input(logic)
    # valid_instructions = get_valid_instructions(instructions, 'E', '#1', 1)
    # print(valid_instructions)

    machine = abstract_machine(states, language, instructions, "temp", instructions[0][0], instructions[0][1], "10", 0)
    # machine.machine_stack.append(machine)
    machine.run_machine()
    print_machine(machine)
    # print("\n")
    # machine.run_machine()
    # print_machine(machine)

main()



