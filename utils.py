def get_inputs():
    print("Enter input:")
    lines = []

    while True:
        user_input = input()

        # 👇️ if user pressed Enter without a value, break out of loop
        if user_input == '':
            break
        else:
            lines.append(user_input)

    return lines


def find_logic_section(inputs: list):
    for i in range(len(inputs)):
        if(inputs[i].strip() == ".LOGIC"):
            return i
    return -1


def find_data_section(inputs: list):
    for i in range(len(inputs)):
        if(inputs[i].strip() == ".DATA"):
            return i
    return -1