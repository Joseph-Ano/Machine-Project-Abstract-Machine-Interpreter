from utils import*
from abstract_machine import*
from memory import*


def main():
    data, logic = get_machine_design()
    # print(data)
    # print(logic)

    # input = "001#"
    # idx = 0

    states, language, memory_language, instructions = parse_logic_input(logic)
    memory = parse_data_input(data)
    # valid_instructions = get_valid_instructions(instructions, 'E', '#1', 1)
    # print(valid_instructions)
    # print(memory.stackDict)
    print(instructions)
    
    # machine = abstract_machine(states, 
    #                            language, 
    #                            instructions, 
    #                            memory, 
    #                            instructions[0][0], 
    #                            instructions[0][1], 
    #                            input, 
    #                            idx)

    # machine.start()
    # machine.run()

    # print_machine(machine)
    # print("\n")

    # machine.step()
    # print_machine(machine)
    # print("\n")
   
    # machine.step()
    # print_machine(machine)
    # print("\n")
   
    # machine.step()
    # print_machine(machine)
    # print("\n")

    # machine.step()
    # print_machine(machine)
    # print("\n")

    # machine.step()
    # print_machine(machine)
    # print("\n")

    # machine.step()
    # print_machine(machine)
    # print("\n")

    # machine.step()
    # print_machine(machine)
    # print("\n")

    # machine.step()
    # print_machine(machine)
    # print("\n")
    

main()



