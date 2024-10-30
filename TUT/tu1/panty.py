import streamlit as st


# Page Setup here
def page_setup():
    # Settting the page width as wide
    st.set_page_config(
        layout="wide",
    )

    p1 = st.Page(
        page="src/Intro.py",
        title="Introduction to panty sniffing",
        icon="👋",
        default=True,
    )

    p2 = st.Page(
        page="src/c1.py",
        title="Ch1",
        icon="👋",
    )
    p3 = st.Page(
        page="src/c2.py",
        title="Ch2",
        icon="👋",
    )

    # -- Setting up the navigation ---
    pg = st.navigation(
        {
            "ArmpitSniff": [p1],
            "PantySniff": [p2, p3],
        },
    )

    img1 = "https://i.ibb.co/9VXhzzP/image.png"
    st.logo(
        img1,
    )
    st.sidebar.warning(
        "This is a sidebar",
    )

    pg.run()


# Execute the main function with pages defined above
def main():
    page_setup()


if __name__ == "__main__":
    main()
