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
input_stext="Input a special number (from 1 to {}):".format(49)
my_special_number=st.number_input(input_stext,step=1,key=6)
click=st.button("Start drawing: ")
all_nums=[i+1 for i in range(49)]
def draw_mark_6(my_nums,my_special_number):
    nums=list(np.random.choice(all_nums,size=7,replace=False))
    nums,special_num=nums[:-1],nums[-1]
    st.text("numbers drawn are:")
    st.text([nums,special_num])
    st.text("your numbers are: ")
    st.text([my_nums,my_special_number])
    nums=set(nums)
    my_nums=set(my_nums)
    if nums==my_nums:
        return "first_prize"
    elif len(nums.intersection(my_nums))==5:
        if my_special_number==special_num:
            return "second prize"
        return "third prize"
    return "nothing"
if click:
    result=draw_mark_6(my_nums,my_special_number)
    st.text(result)