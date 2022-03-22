import streamlit as st
import numpy as np
import pandas as pd

st.title("Welcome to mark six")
st.header("Pick 6 numbers")
my_nums=[]
for i in range(6):
    input_text="Input a number (from 1 to {}):".format(49)
    number=st.number_input(input_text,step=1,key=i)
    my_nums.append(number)
click=st.button("Start drawing: ")
all_nums=[i+1 for i in range(49)]
def draw_mark_6(my_nums):
    my_nums.sort()
    nums=list(np.random.choice(all_nums,size=6,replace=False))
    nums.sort()
    st.text("numbers drawn are:")
    st.text(nums)
    st.text("your numbers are: ")
    st.text(my_nums)
    if nums==my_nums:
        return "success"
    else:
        return "fail"
if click:
    result=draw_mark_6(my_nums)
    st.text(result)