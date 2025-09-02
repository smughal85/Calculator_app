import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Streamlit Calculator")

# User input
num1 = st.number_input("Enter first number:", value=0.0, format="%.4f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.4f")

operation = st.selectbox("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation
result = None
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("❌ Division by zero is not allowed.")

# Show result
if result is not None:
    st.success(f"Result: **{result}**")
