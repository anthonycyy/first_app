import streamlit as st
import pandas as pd

st.title("Hello")
st.header("Data science is the best")
my_str=st.text_input("name?")
threshold=st.number_input("preferred length?")

click_ans=st.button("enter")
def f(my_str,threshold):
    st.text(f'My string is {my_str}')
    if len(my_str)>threshold:
        st.text( "long string")
    else:
        st.text( "short string")
if click_ans:
    f(my_str)

click=st.button("snow")
arr=[i for i in range(10)]
bar=st.sidebar.select_slider('slide it',options=arr)

if click:
  st.snow()
  st.text('snow is coming')