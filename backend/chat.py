# Chat with Pato using an anthropic model

import anthropic
import streamlit as st
import os

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def chat_with_pato(message):
    system_prompt = """You are Pato, a super Data Engineer from Guadalajara, Mexico. 
    You have expertise in various data engineering projects including:
    - Building scalable ETL pipelines
    - Database optimization and indexing
    - Data cleaning and normalization processes
    - Big data processing frameworks
    - Cloud-based data warehousing
    - Real-time data streaming architectures

    You are enthusiastic about helping others learn about data engineering and sharing your experiences.
    You are passionate about data systems and infrastructure.
    Your hobbies include exploring new data technologies and contributing to open-source data projects.
    You are known for your ability to optimize data workflows and improve system efficiency.
    You enjoy mentoring junior engineers in best practices for data pipeline development.
    Respond naturally and professionally to questions about your projects, skills, and journey in data engineering."""

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {
                "role": "user", 
                "content": message
            }
        ],
    )
    return response.content[0].text

def show_chat_history(messages):
    for message in messages:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user-message">
                    <div class="message-content">
                        {message["content"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message assistant-message">
                    <div class="message-content">
                        {message["content"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)

def show_project():
    st.markdown("""
        <div class="project-card chat-header">
            <h1>Chat with Me</h1>
            <p>Welcome! I'm Pato, a Data Engineer here to share insights about data pipelines and engineering solutions.</p>
            <div class="skill-tag">ETL Pipelines</div>
            <div class="skill-tag">Database Optimization</div>
            <div class="skill-tag">Data Engineering</div>
        </div>
    """, unsafe_allow_html=True)

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    show_chat_history(st.session_state.chat_history)

    # Chat input
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([4, 1])  # Create two columns with ratio 4:1
    with col1:
        question = st.text_input("", placeholder="Ask me anything...", key="chat_input")
    with col2:
        send_button = st.button("Send", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if send_button and question:  # Check if button is clicked and question is not empty
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": question})
        
        # Get and add assistant response
        response = chat_with_pato(question)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Rerun to update chat display
        st.rerun()

    # Add custom CSS
    st.markdown("""
        <style>
        .chat-header {
            margin-bottom: 2rem;
            text-align: center;
        }

        .chat-message {
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 10px;
            max-width: 80%;
        }

        .user-message {
            background-color: #2E4057;
            color: white;
            margin-left: auto;
        }

        .assistant-message {
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            margin-right: auto;
        }

        .message-content {
            word-wrap: break-word;
        }

        .chat-input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 1rem;
            background-color: white;
            border-top: 1px solid #e9ecef;
            z-index: 1000;
        }

        .stTextInput > div > div > input {
            border-radius: 20px;
            padding: 0.75rem 1.5rem;
            border: 2px solid #e9ecef;
        }

        .stTextInput > div > div > input:focus {
            border-color: #2E4057;
            box-shadow: 0 0 0 2px rgba(46,64,87,0.2);
        }

        .skill-tag {
            display: inline-block;
            background: #e9ecef;
            padding: 0.25rem 0.75rem;
            border-radius: 16px;
            margin: 0.25rem;
            font-size: 0.875rem;
            color: #2E4057;
        }

        /* Add styles for the send button */
        .stButton button {
            border-radius: 20px;
            background-color: #2E4057;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            height: 100%;
        }

        .stButton button:hover {
            background-color: #1a2633;
        }
        </style>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show_project()  