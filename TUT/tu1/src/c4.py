import streamlit as st
import pandas as pd


def B4() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("Chapter 4 - Chart Elements")


################
# Execution
B4()
