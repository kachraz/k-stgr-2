import streamlit as st


# Page Setup here
def page_setup():
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
        pages=[pg1, pg2, pg3],
    )

    pg.run()


# Execute the main function with pages defined above
def main():
    page_setup()


if __name__ == "__main__":
    main()
