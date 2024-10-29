import streamlit as st
from src.u import pic_func


def hero1() -> None:
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
    with col1:
        st.title("Page 2 - Hero Section")
        pic_func()

    with col2:
        st.title("Page 2 - Hero Section")


def main_page_function() -> None:
    st.title("Page 2")
    hero1()


# Execute Function
main_page_function()
