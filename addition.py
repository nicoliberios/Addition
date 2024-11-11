import streamlit as st

st.title("Sum of Two Numbers")
st.image("Foto/suma.png", width=300)
st.header("Nicolas Liberio")

# Prompt the values to sum
number1 = st.number_input("Please enter the first number:", format="%.2f")
number2 = st.number_input("Please enter the second number:", format="%.2f")

# Button to perform the addition
if st.button("Add"):
    # Add the numbers
    result = number1 + number2
    
    # Display the result
    st.success(f"The result of the addition is: {result}")
