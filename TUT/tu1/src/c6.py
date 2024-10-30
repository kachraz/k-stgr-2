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
    "## Slider Function"
    min_val, max_val = st.slider(
        "Select a Range of Values",
        0.0,
        100.0,
        (25.0, 75.0),
    )
    st.write("Values:", min_val, max_val)

    # Another one
    m_v = st.slider("Set Min Val", 0, 50, 25)
    st.write("Min Val:", m_v)
    sl_va = st.slider("Panty", m_v, 100, m_v)
    st.write("Panty:", sl_va)


##################################
# Page Execution
B6()
