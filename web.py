import streamlit as st
import functions as f

todos = f.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)


st.title("Yoshi's Todo App")
st.write("Have fun bitches!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a listy thing", placeholder="Add a new todo :)",
              on_change=add_todo, key="new_todo")
