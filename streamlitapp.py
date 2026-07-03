import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Calculator")
st.write("A simple calculator built with Streamlit.")

# Number inputs
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed.")
            st.stop()

    st.success(f"Result: {result}")

st.markdown("---")
st.caption("Developed by Yash Mittal")
