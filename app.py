import streamlit as st
import numpy as np
import pandas as pd

st.title("Welcome to mark six")
st.header("Pick 6 numbers")
my_nums=[]
for i in range(6):
    number=st.number_input("Input a number: ",step=1,key=i)
    my_nums.append(number)
click=st.button("Start drawing: ")
all_nums=[i+1 for i in range(49)]
def draw_mark_6():
    all_nums=np.random.choice(all_nums,size=6,replace=False)
    st.text(all_nums)
if click:
    draw_mark_6()