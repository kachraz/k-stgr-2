import streamlit as st


# Page Setup here
def page_setup():
    # Settting the page width as wide
    st.set_page_config(layout="wide")

    pg1 = st.Page(
        page="src/pag1.py",
        title="Page 1",
        icon="👋",
        default=True,
    )

    pg2 = st.Page(
        page="src/pag2.py",
        title="Page 2",
        icon="👋",
    )
    pg3 = st.Page(
        page="src/pag3.py",
        title="Page 3",
        icon="👋",
    )

    # -- Setting up the navigation ---
    pg = st.navigation(
        {
            "ArmpitSniff": [pg1],
            "PantySniff": [pg2, pg3],
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
