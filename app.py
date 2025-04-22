import streamlit as st
import math

st.title("🧮 Enhanced Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Dropdown menu for selecting the operation
operation = st.selectbox(
    "Select an operation:",
    (
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)",
        "Exponentiation (^)",
        "Modulus (%)",
        "Square Root (√)",
        "Logarithm (log)"
    )
)

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
            st.success(f"Result: {result:.2f}")
        elif operation == "Subtraction (-)":
            result = num1 - num2
            st.success(f"Result: {result:.2f}")
        elif operation == "Multiplication (×)":
            result = num1 * num2
            st.success(f"Result: {result:.2f}")
        elif operation == "Division (÷)":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Result: {result:.2f}")
            else:
                st.error("Error: Division by zero is not allowed.")
        elif operation == "Exponentiation (^)":
            result = num1 ** num2
            st.success(f"Result: {result:.2f}")
        elif operation == "Modulus (%)":
            if num2 != 0:
                result = num1 % num2
                st.success(f"Result: {result:.2f}")
            else:
                st.error("Error: Modulus by zero is not allowed.")
        elif operation == "Square Root (√)":
            if num1 >= 0:
                result = math.sqrt(num1)
                st.success(f"Square root of {num1} is {result:.2f}")
            else:
                st.error("Error: Cannot compute square root of a negative number.")
        elif operation == "Logarithm (log)":
            if num1 > 0:
                result = math.log(num1)
                st.success(f"Natural logarithm of {num1} is {result:.2f}")
            else:
                st.error("Error: Logarithm undefined for non-positive numbers.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
