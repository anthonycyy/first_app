import streamlit as st
import pandas as pd

st.title("Hello")
st.header("Data science is the best")
my_str=st.text_input("name?")
st.text(f'My string is {my_str}')

click=st.button("press me")
arr=[i for i in range(10)]
bar=st.sidebar.select_slider('slide it',options=arr)

if click:
  st.snow()
  st.text('snow is coming')

def f(my_str,threshold=10):
  if len(my_str)>threshold:
    return ( "long string")
  else:
    return ( "short string")
st.text(f(my_str))