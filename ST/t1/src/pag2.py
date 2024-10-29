import streamlit as st
from src.u import pic_func


def main_page_function() -> None:
    st.title("Page 2")
    pic_func()


# Execute Function
main_page_function()
