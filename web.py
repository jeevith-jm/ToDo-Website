import streamlit as st
import functions
import time


st.set_page_config(
    page_title="ToDo's",
    page_icon="📝",
    initial_sidebar_state="collapsed",
)
hide_menu_style=("""
                <style> 
                footer {visibility: hidden;}
                </style>
                 """)
st.markdown(hide_menu_style,unsafe_allow_html=True)
todos = functions.read_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title('''To-Do's :ballot_box_with_check:''')
st.divider()
st.write("<b>Keep In Track Of Your Daily Tasks</b>",unsafe_allow_html=True)
display=time.strftime("%b %d, %Y")
st.write(f'''<b>It's {display}</b>''',unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checklist = st.checkbox(f''':black[{todo}]''', key=todo)
    if checklist:
        st.toast('''Yay!!Task Completed:confetti_ball:''')
        time.sleep(1)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


input = st.text_input(label="",placeholder="Add a new todo",
                      on_change=add_todo, key="new_todo")
if input:
    st.toast('''ToDo Added Successfully :tada:''')
    time.sleep(.5)

def clear_text():
    st.session_state["new_todo"] = ""


st.button("Clear Text", type="primary",on_click=clear_text)
