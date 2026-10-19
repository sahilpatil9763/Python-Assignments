"""
3: Simple Interest Calculator

Develop a Streamlit application that accepts Principal Amount, Rate of Interest and Time Period.
Provide a Calculate button to calculate and display the Simple Interest.
"""

import streamlit as st

# Application title

st.title("Simple Interest Calculator")

p = st.text_input("Enter Principal Amount:")
r = st.text_input("Enter Rate of Interest:")
t = st.text_input("Enter Time in Years:")

if st.button("Calculate"):
    p = float(p)
    r = float(r)
    t = float(t)

    si = (p * r * t) / 100

    st.success(f"Simple Interest is: ₹{si}")