import streamlit as st

# markdown for beign called
m1 = """
# App Desc

All the work being done here is from this [Tutorial](https://youtu.be/o8p7uQCGD0U?si=YzpFGQLhCIKf3RxT)

[![](https://i.ytimg.com/an_webp/o8p7uQCGD0U/mqdefault_6s.webp?du=3000&sqp=CKCmiLkG&rs=AOn4CLDIza7ordoY6lSS_H4cRqSxRl7H_A)](https://youtu.be/o8p7uQCGD0U?si=YzpFGQLhCIKf3RxT)

1. Rest of the pages will have the work for this

## Chapter Descriptions 

Chapter | WTF 
--- | ---
c1 | Starter Code
"""


def bodu() -> None:
    st.image("https://i.ibb.co/DL6R0Bf/New-Project.png")
    st.markdown(m1)


def pagez() -> None:
    st.markdown("## Navigation")
    co1, co2 = st.columns(2)

    with co1:
        st.page_link("src/Intro.py", label="Home", icon="🏠")
        st.page_link("src/c1.py", label="Chapter 1", icon="1️⃣")
        st.page_link("src/c2.py", label="Chapter 2", icon="2️⃣")
        st.page_link("src/c3.py", label="Chapter 3", icon="3️⃣")
        st.page_link("src/c4.py", label="Chapter 4", icon="4️⃣")

    with co2:
        st.write("Home Page")
        st.write("General panty")
        st.write("Chatper 2 - Focus on text elements")
        st.write("Chatper 3 - Data Elements")
        st.write("Chatper 4 - Chart Elements")


# Call Page Function
bodu()
pagez()
