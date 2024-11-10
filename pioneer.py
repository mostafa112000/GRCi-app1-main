import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def app():
    
    # App title
    st.title("`Pioneer+` ")
    # Load the tokenizer and model
    @st.cache_resource
    def load_model():
        MODEL_NAME = "distilgpt2"  # A smaller model for testing
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32)
        return tokenizer, model

    tokenizer, model = load_model()

    # Function to generate response
    def generate_response(prompt):
        inputs = tokenizer(prompt, return_tensors="pt")
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.95
        )
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response[len(prompt):].strip()

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
