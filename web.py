import streamlit as st
import functions

def add_task():
    new_task = st.session_state['new_task'] + '\n'
    tasks.append(new_task)
    functions.write_file(tasks)


tasks = functions.open_file()

st.title('My Tasks App')

for task in tasks:
    st.checkbox(task)

st.text_input(label='', placeholder='Add a new task...',
              on_change=add_task, key='new_task')