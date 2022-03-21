import streamlit as st

st.title("Hello")
st.header("DS4 is the best")
my_str=st.text_input("name?")
st.text(f'Hello {my_str}')

def f(my_str):
  if len(my_str)>10:
    return "long string"
  else:
    return "short string"
st.text(f'{f(my_str)}')
