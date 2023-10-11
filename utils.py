def get_inputs():
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