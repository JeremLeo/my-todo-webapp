import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].capitalize() + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def complete_todo():
    pass


st.title("My Todo App")
st.subheader("This is a Todo App")
st.write("Increase your productivity")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")

st.session_state