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


# Call Page Function
bodu()
