import streamlit as st

def app():
    st.title('`Account`')
    st.header('Name: '+st.session_state.username)
    st.text('Email id: '+st.session_state.useremail)

    