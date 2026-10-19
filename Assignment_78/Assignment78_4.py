"""
4: Student Result Calculator

Develop a Streamlit application that accepts a student's name and marks in three subjects. Calculate total marks,
percentage and display whether the student has passed or failed. Consider 40 marks out of 100 as the minimum
passing marks in each subject.
"""


import streamlit as st

# Application Title
st.title("🎓 Student Result Calculator")
st.caption("✨ Calculate your total marks, percentage and result")

st.divider()

# Student Details
st.subheader("👤 Student Details")

name = st.text_input("Enter Student Name")

st.subheader("📚 Enter Subject Marks")

maths = st.number_input("Mathematics (out of 100)", min_value=0, max_value=100, step=1)
science = st.number_input("Science (out of 100)", min_value=0, max_value=100, step=1)
english = st.number_input("English (out of 100)", min_value=0, max_value=100, step=1)

st.divider()

# Calculate Button
if st.button("📊 Calculate Result", use_container_width=True):

    if name.strip() == "":
        st.warning("Please enter the student's name.")

    else:
        total = maths + science + english
        percentage = (total / 300) * 100

        st.header(f"🏆 Result of {name}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Marks", f"{total} / 300")

        with col2:
            st.metric("Percentage", f"{percentage:.2f}%")

        # Check pass or fail in every subject
        if maths >= 40 and science >= 40 and english >= 40:
            st.success("🎉 PASS — Congratulations!")
            st.balloons()
        else:
            st.error("❌ FAIL — Minimum 40 marks are required in each subject.")
