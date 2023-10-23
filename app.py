import streamlit as st
from utils import*

def main():
    form = st.form(key='main_form')
    user_input = form.text_input('Enter Input', key="user_input")
    machine_design = form.text_area("Code area", height=250, key="machine_design")
    runBtn = form.form_submit_button('run')

    if(runBtn):
        data, logic = app_get_machine_design(machine_design.splitlines())

        if(user_input == ""):
            print("Missing User Input")
        elif(len(data) == 0 and len(logic) == 0):
            print("Missing Machine Design")
        else:
            print(f"{user_input}\n{data}\n{logic}")

if __name__ == "__main__":
    main()