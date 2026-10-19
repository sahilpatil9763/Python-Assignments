"""
1: Addition of Two Numbers
Develop a Streamlit application that accepts two numbers from the user using input fields. Provide an Add
button to calculate and display the addition of the entered numbers.
"""


import streamlit as st

# Application title
st.title("Addition of Two Numbers")

# Accept input from the user
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

# Add button
if st.button("Add"):
    result = num1 + num2
    st.success(f"Addition: {num1} + {num2} = {result}")