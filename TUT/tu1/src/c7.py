# You are doing your tests here
import streamlit as st


def B7() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("C7 - Personal Tests")

    st.divider()

    "## Testing Applying Function on value"
    with st.container():
        number = st.number_input("Insert a number", min_value=0, max_value=10)
        st.write("The current number is ", number)
        if number > 5:
            st.success("The number is greater than 5")
        else:
            st.error("The number is less than 5")

    st.divider()
    "## Taken from manual submit form "
    with st.container(border=True):
        with st.form("my_form"):
            st.write("Inside the form")
            slider_val = st.slider("Form slider", min_value=0, max_value=10)
            checkbox_val = st.checkbox("Form checkbox")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("slider", slider_val, "checkbox", checkbox_val)


#######################
# Execution
B7()
