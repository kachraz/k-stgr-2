import streamlit as st


def B1() -> None:
    st.header("Chapter 1 - General Panties ")

    st.write("Hello, World! From Chapter 1")
    st.write("Hello, World! From Chapter 1")
    st.write("Hello, World! From Chapter 1")

    st.divider()

    # Testing the object here
    st.write("Testing Json Object Printin")
    st.write(
        {
            "Chapter 1": "https://youtu.be/o8p7uQCGD0U?si=YzpFGQLhCIKf3RxT",
            "Chapter 2": "https://youtu.be/o8p7uQCGD0U?si=YzpFGQLhCIKf3RxT",
        }
    )
    st.write(True)
    st.write(123)

    # Next section
    st.divider()
    23 + 88

    # This solves the issue of writing markdown in an easy way
    # These are called magics

    "# Why panties are the best"
    "![](data:image/jpeg;base64,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)"

    # Button
    st.divider()
    "> Testing buttonhere"
    print("panty")
    pr = st.button("LickMe")
    print(pr)


# Execiting the page function
B1()
