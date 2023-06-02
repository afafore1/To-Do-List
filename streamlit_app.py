import streamlit as st

def main():
    st.title("To-Do List App")

    task_list = st.session_state.get('task_list', [])

    new_task = st.text_input("New Task")

    if new_task:
        task_list.append(new_task)
        st.session_state['task_list'] = task_list

    if st.button("Clear Tasks"):
        task_list.clear()
        st.session_state['task_list'] = task_list

    for task in task_list:
        st.write(task)

if __name__ == "__main__":
    main()
