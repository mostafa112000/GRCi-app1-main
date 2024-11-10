import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import subprocess

def app():

    # App title
    st.title("`Pioneer+` ")
    #st.header("`Chat`")

    # Sidebar configuration for user inputs
    #with st.sidebar:
        #max_tokens = st.slider('Max Tokens', 10, 500, 100)
        #temperature = st.slider('Temperature', 0.0, 1.0, 0.7, 0.05)

    # Function to generate response using Ollama
    def generate_response(prompt):
        try:
            # Run the Ollama model with the given prompt
            result = subprocess.run(
                ["ollama", "run", "llama3.2:1b"],
                input=prompt,
                text=True,
                capture_output=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            st.error(f"Error: {e.stderr}")  # Display the detailed error in Streamlit
            return "An error occurred while generating the response."

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input and response display
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear chat history function and button
    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)
