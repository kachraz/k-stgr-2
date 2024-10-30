import streamlit as st
import pandas as pd


def B3() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()
    "# Testing Data Elemenets"

    "Data Frames"

    df = pd.DataFrame(
        {
            "first column": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "second column": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            "Names": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        }
    )

    st.dataframe(df.style.highlight_max(axis=0))

    "## Making it editable"
    edit_df = st.data_editor(df, use_container_width=True)

    "Make the same into a table"
    "? Tables are not editable and you can extract values from them , with dataframes you can"
    st.table(edit_df)

    st.divider()
    "## Metrics Section"
    st.metric(label="Temperature", value="70 °F", delta="+1.2 °F")

    st.divider()

    st.divider()


def B3Charts() -> None:
    df = pd.DataFrame(
        {
            "first column": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "second column": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            "Names": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        }
    )

    "## Charts"
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.bar_chart(df)
    with c2:
        st.line_chart(df)
    with c3:
        st.area_chart(df)
    with c4:
        st.write("Testing charts here")


#######################
# Execution
B3()
B3Charts()
