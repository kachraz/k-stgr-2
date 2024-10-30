import streamlit as st
import os


def B2() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("Chapter 2 - Text Elements")

    st.divider()
    st.title("Chapter 2 Title")
    st.header("Chapter 2 Header")
    st.subheader("Chapter 2 Subheader")
    st.markdown("## Chapter 2 _Markdown_")
    st.caption("Chapter 2 _Caption_")

    "> Writing Code in Streamlit"
    st.code(
        """
from panties import juice
def drinkJuice():
    print("Drink Juices")
""",
        line_numbers=True,
        language="python",
    )

    with st.echo():
        st.divider()

    st.divider()
    "Making Images"
    st.image("https://picsum.photos/200")
    st.image(
        "https://raw.githubusercontent.com/kachraz/k-stgr-2/refs/heads/main/kh/1z.jpg",
        width=50,
    )

    st.divider()


####################################
# Execute page functin
B2()
