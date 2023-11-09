import streamlit as st
from abstract_machine import abstract_machine
from utils import*

ACCEPT_RESPONSE = "Input is accepted"
REJECT_RESPONSE = "Input is rejected"

def get_machine_info(machine):
    stack_contents = f"Stack:\n{machine.memory.print_stack_contents()}"
    queue_contents = f"Queue:\n{machine.memory.print_queue_contents()}"
    tape1_contents = f"Tape 1d:\n{machine.memory.print_tape_contents()}"
    current_input_state = f"Input State: {get_current_input_state(machine.curInputIdx, machine.input)}"
    current_machine_state = f"Current State: {machine.curState}"

    return stack_contents, queue_contents, tape1_contents, current_input_state, current_machine_state


def main():
    form = st.form(key='main_form')
    user_input = form.text_area('Enter Input', height=100, key="user_input")
    input_type = form.radio("Type of input", options=["Single", "Multiple"])
    machine_design = form.text_area("Code area", height=250, key="machine_design")
    loadBtn = form.form_submit_button('Load')

    if(input_type == "Single"):
        stepBtn = st.button("Step")
    else:
        runBtn = st.button("Run")

    if(loadBtn):
        data, logic = app_get_machine_design(machine_design.splitlines())

        if(user_input == ""):
            st.text("Missing User Input")
        elif(len(data) == 0 and len(logic) == 0):
            st.text("Missing Machine Design")
        else:
            # print(f"User input: {user_input}\nData Section:\n{data}\nLogic Section:\n{logic}")
            states, language, memory_language, instructions = parse_logic_input(logic)
            # print(instructions)
            user_input = user_input.splitlines()
            machines = []

            for input in user_input:
                memory = parse_data_input(data, input)
                machine = abstract_machine(states, 
                               language, 
                               instructions, 
                               memory, 
                               instructions[0][0], 
                               instructions[0][1], 
                               input, 
                               0)
                machines.append(machine)

            if(input_type == "Single"):
                cur_machine = machines[0]
                cur_machine.start()
                stack_contents, queue_contents, tape1_contents, current_input_state, current_machine_state = get_machine_info(cur_machine)
            
                # Shows state/content of each memory
                st.text(stack_contents)
                st.text(queue_contents)
                st.text(tape1_contents)

                # Shows current state of input
                st.text(current_input_state)
                # Shows current state of machine
                st.text(current_machine_state)
            
                # stores starting state of machine
                st.session_state["machine"] = cur_machine
            else:
                st.session_state["machine"] = machines

    if(input_type == "Single"):
        if(stepBtn and "machine" not in st.session_state):
            st.text("Load a machine before pressing step")

        elif(stepBtn and st.session_state["machine"] is None):
            st.text("Already finished previous run. Load a new machine to run again")

        elif(stepBtn):
            cur_machine = st.session_state["machine"]
            cur_machine.step()
            st.session_state["machine"] = cur_machine
            print_machine(cur_machine)
            # print("\n")
        
            stack_contents, queue_contents, tape1_contents, current_input_state, current_machine_state = get_machine_info(cur_machine)
            
            # Shows state/content of each memory
            st.text(stack_contents)
            st.text(queue_contents)
            st.text(tape1_contents)

            # Shows current state of input
            st.text(current_input_state)
            # Shows current state of machine
            st.text(current_machine_state)


            if(cur_machine.curState == "accept"):
                st.session_state["machine"] = None
                st.text(ACCEPT_RESPONSE)

            elif((len(cur_machine.machine_stack) == 0 and len(cur_machine.valid_instructions) == 0) or cur_machine.curState == "reject"):
                st.session_state["machine"] = None
                st.text(REJECT_RESPONSE)
    else:
        if(runBtn and "machine" not in st.session_state):
            st.text("Load a machine before pressing step")

        elif(runBtn and st.session_state["machine"] is None):
            st.text("Already finished previous run. Load a new machine to run again")

        elif(runBtn):
            machines = st.session_state["machine"]
            for i in range(0, len(machines)):
                cur_machine = machines[i]
                cur_machine.run()

                if(cur_machine.curState == "accept"):
                    st.text(f"{cur_machine.input}: {ACCEPT_RESPONSE}")

                elif((len(cur_machine.machine_stack) == 0 and len(cur_machine.valid_instructions) == 0) or cur_machine.curState == "reject"):
                    st.text(f"{cur_machine.input}: {REJECT_RESPONSE}")

            st.session_state["machine"] = None          

if __name__ == "__main__":
    main()



# show the state and values
# in each memory object during each step of the input. Optionally, you can ask for multiple inputs and show the outputs for each
# input without showing the machine state step-by-step