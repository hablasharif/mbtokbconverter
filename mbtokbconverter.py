import streamlit as st

# Page title
st.title("MB to KB Converter")

# Input field for entering MB
mb_input = st.number_input("Enter the size in megabytes (MB):")

# Convert MB to KB
kb_result = mb_input * 1000

# Display the result
st.write(f"{mb_input} MB is equal to {kb_result} KB")
