"""
5: Celsius to Fahrenheit Converter

Develop a Streamlit application that accepts temperature in Celsius. Provide a Convert button to convert the 
entered temperature into Fahrenheit and display the result.
"""


import streamlit as st

# Application Title
st.title("🌡️ Temperature Converter")
st.caption("Convert Celsius into Fahrenheit easily!")

st.divider()

# Input Temperature
celsius = st.number_input("Enter Temperature in Celsius:")

# Convert Button
if st.button("🔄 Convert", use_container_width=True):
    fahrenheit = (celsius * 9 / 5) + 32

    st.divider()
    st.subheader("🌞 Conversion Result")
    st.success(f"{celsius}°C = {fahrenheit:.2f}°F")