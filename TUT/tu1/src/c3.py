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
    "## Charts"
    st.bar_chart(df)
    st.line_chart(df)
    st.area_chart(df)
    st.area_chart(edit_df)

    st.divider()
    "## Maps"


#######################
# Execution
B3()
