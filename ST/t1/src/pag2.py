import streamlit as st
from src.u import pic_func


# Form Code
def form2() -> None:
    with st.form("my_form"):
        st.write("Inside the form")
        slider = st.slider("Select a number")
        checkbox = st.checkbox("I agree the terms and conditions")
        submitted = st.form_submit_button("Submit")


@st.dialog("Suck and Fuck")
def form1() -> None:
    st.text_input("Inside the form")


# Hero Section Code
def hero1() -> None:
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
    with col1:
        st.title("Page 2 - Hero Section")
        pic_func()

    with col2:
        st.title("Page 2 - Hero Section")

        # Button Function
        if st.button("Click me!"):
            form1()


def main_page_function() -> None:
    st.title("Page 2")
    hero1()


# Execute Function
main_page_function()
