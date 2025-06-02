# Create a task manager for the projects (include 3 status due to do, in progress, done)

import streamlit as st

def show_project():
    st.title("Task Manager")
    
    # Custom CSS for columns
    st.markdown("""
        <style>
        [data-testid="stExpander"] {
            background-color: #f0f2f6;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #e0e0e0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Initialize tasks in session state if not exists
    if 'tasks' not in st.session_state:
        st.session_state.tasks = {
            'To Do': [],
            'In Progress': [],
            'Done': []
        }
    
    # Create new task
    with st.form("new_task", border=True):
        st.markdown("### Create New Task")
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Task Description")
        submitted = st.form_submit_button("Add Task", type="primary")
        
        if submitted and task_title:
            st.session_state.tasks['To Do'].append({
                'title': task_title,
                'description': task_description
            })
    
    # Display tasks in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <h3 style='text-align: center; color: #ff4b4b; background-color: #ffe6e6; 
            padding: 10px; border-radius: 5px;'>To Do</h3>
        """, unsafe_allow_html=True)
        for i, task in enumerate(st.session_state.tasks['To Do']):
            with st.expander(task['title']):
                st.write(task['description'])
                if st.button('➡️ Move to In Progress', key=f'todo_{i}', type="primary"):
                    st.session_state.tasks['In Progress'].append(task)
                    st.session_state.tasks['To Do'].pop(i)
                    st.rerun()
    
    with col2:
        st.markdown("""
            <h3 style='text-align: center; color: #ff9d00; background-color: #fff4e6; 
            padding: 10px; border-radius: 5px;'>In Progress</h3>
        """, unsafe_allow_html=True)
        for i, task in enumerate(st.session_state.tasks['In Progress']):
            with st.expander(task['title']):
                st.write(task['description'])
                col_left, col_right = st.columns(2)
                with col_left:
                    if st.button('⬅️ Move to To Do', key=f'inprog_todo_{i}'):
                        st.session_state.tasks['To Do'].append(task)
                        st.session_state.tasks['In Progress'].pop(i)
                        st.rerun()
                with col_right:
                    if st.button('➡️ Move to Done', key=f'inprog_done_{i}', type="primary"):
                        st.session_state.tasks['Done'].append(task)
                        st.session_state.tasks['In Progress'].pop(i)
                        st.rerun()
    
    with col3:
        st.markdown("""
            <h3 style='text-align: center; color: #00c853; background-color: #e6ffe6; 
            padding: 10px; border-radius: 5px;'>Done</h3>
        """, unsafe_allow_html=True)
        for i, task in enumerate(st.session_state.tasks['Done']):
            with st.expander(task['title']):
                st.write(task['description'])
                if st.button('⬅️ Move to In Progress', key=f'done_{i}'):
                    st.session_state.tasks['In Progress'].append(task)
                    st.session_state.tasks['Done'].pop(i)
                    st.rerun()

if __name__ == "__main__":
    show_project()