import streamlit as st
import pandas as pd


############# Form function here ################
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


def form2() -> None:
    # This is your custom form which you are writing here
    st.title("User Info")
    with st.form(key="my_form", clear_on_submit=True):
        name = st.text_input("Enter your name :")
        age = st.number_input("Enter your age :")
        submit = st.form_submit_button("Submit")
    if submit:
        st.write(f"Your name is {name} and age is {age}")
        st.image("https://i.ibb.co/0Mwq0Yk/IMG-20220818-WA0000.jpg")


def form3() -> None:
    # This is your custom form which you are writing here
    # When you do it this way the form button is outside
    fo_val = {
        "Name": st.text_input("Enter your name :"),
        "Age": st.number_input("Enter your age :"),
        "Gender": st.radio(
            "Select your gender :", ("Male", "Female", "Other", "Rapist")
        ),
    }
    with st.form(key="my_f3", clear_on_submit=True):
        submit = st.form_submit_button("Submit")
    if submit:
        if not all(fo_val.values()):
            st.error("Please fill all the fields")
        else:
            st.toast("Form Submitted")
            st.snow()
            st.write(
                f"Your name is {fo_val['Name']} and age is {fo_val['Age']} and gender is {fo_val['Gender']}"
            )


########## MAIN FUNCTION ##########
def B5() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("Chapter 5 - Form")
    form1()

    st.divider()
    "## New one here"
    form2()

    st.divider()
    "## New Cstom Form"
    form3()


######
# Execution of page
B5()
