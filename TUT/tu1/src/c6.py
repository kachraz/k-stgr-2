import streamlit as st


def B6() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("Chapter 6 - Advanced Forms")

    st.divider()

    "This is a button with a container"
    with st.container(border=True):
        b1 = st.button("Open Dialog")
        if b1:
            st.warning("WARNING")

    st.divider()


##################################
# Page Execution
B6()
