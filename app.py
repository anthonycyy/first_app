import streamlit as st
import numpy as np
import pandas as pd

st.title("Welcome to mark six")
st.header("Pick 6 numbers")
my_nums=[]
for _ in range(1):
    number=st.number_input("Input a number: ",step=1)
    # my_nums.append(number)
# click_ans=st.button("enter")
