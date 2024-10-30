import streamlit as st


def B2() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("Chapter 2 - Text Elements")


####################################
# Execute page functin
B2()
