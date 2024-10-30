import streamlit as st
import pandas as pd


# Form function here
def form1() -> None:
    c1, c2 = st.columns(2)
    with c1:
        # Form 1 here
        with st.form(key="my_f", clear_on_submit=True):
            name = st.text_input(label="Name")
            age = st.number_input(label="Age", step=1)
            submit = st.form_submit_button(label="Submit")
        if submit:
            st.write(f"Your name is {name} and age is {age}")
            st.write("Form here")

        # Form 2
        with st.form(key="my_f1", clear_on_submit=True):
            name = st.text_input(label="Name")
            age = st.number_input(label="Age", step=1)
            submit = st.form_submit_button(label="Submit")
        if submit:
            st.write(f"Your name is {name} and age is {age}")
            st.write("Form here")

    with c2:
        with st.form(key="my_f2", clear_on_submit=True):
            name = st.text_input(label="Name")
            age = st.number_input(label="Age", step=1)
            submit = st.form_submit_button(label="Submit")
        if submit:
            st.write(f"Your name is {name} and age is {age}")
            st.write("Form here")


def B5() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("Chapter 5 - Form")
    form1()

    st.divider()
    "## New one here"


######
# Execution of page
B5()
