import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Chart data here to be used in the functions
c_d1 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
)

scatter_data = pd.DataFrame(
    {
        "x": np.random.randn(100),
        "y": np.random.randn(100),
    }
)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)


def B4() -> None:
    st.page_link("src/Intro.py", label="Home", icon="⬅️", use_container_width=True)
    st.divider()

    st.header("Chapter 4 - Chart Elements")

    st.divider()
    st.area_chart(c_d1)
    st.bar_chart(c_d1)
    st.line_chart(c_d1)

    st.divider()
    st.write("Scatter Plot")
    st.scatter_chart(scatter_data)

    st.divider()
    st.write("Map Plot")
    st.dataframe(map_data, use_container_width=True)
    st.map(map_data)


################
# Execution
B4()
