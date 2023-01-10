import streamlit as st
import functions

def add_task():
    new_task = st.session_state['new_task'] + '\n'
    tasks.append(new_task)
    functions.write_file(tasks)
    st.session_state['new_task'] = ' '


tasks = functions.open_file()

st.title('My Tasks App')
st.write('Check the task when complete')

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_file(tasks)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label=' ', placeholder='Add a new task...',
              on_change=add_task, key='new_task')