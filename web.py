import streamlit as st
import functions

tasks = functions.open_file()

st.title('My Tasks App')

for task in tasks:
    st.checkbox(task)

st.text_input(label='', placeholder='Add a new task...')