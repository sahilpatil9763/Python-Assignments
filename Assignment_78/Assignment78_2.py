"""
2: Even or Odd Number

Develop a Streamlit application that accepts an integer from the user. 
Provide a Check button to determine whether the entered number is even or odd and display the result.
"""


import streamlit as st

# Application title
st.title("Even or Odd Number Checker")

# Accept an integer from the user
num = st.number_input(
    "Enter an integer:",
    value=0,
    step=1
)

# Check button
if st.button("Check"):
    if num % 2 == 0:
        st.success(f"{int(num)} is an Even Number.")
    else:
        st.info(f"{int(num)} is an Odd Number.")