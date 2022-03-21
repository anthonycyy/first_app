import streamlit as st

st.title("Hello")
st.header("DS4 is the best")
my_str=st.text_input("name?")
st.text(f'Hello {my_str}')
