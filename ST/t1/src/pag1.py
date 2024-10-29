import streamlit as st
from src.u import pic_func


def mark_down_test() -> None:
    mktext = """
# Testing out this as a variable 
> Lets see if it can take it or not 
1. Now we cbeck a number

Now lets add able and see what it do 

A | B | C
---|---|---
sniff | her | ass
sniff | her | ass
sniff | her | ass
sniff | her | ass

Everyday 
"""
    code = """
import ass and pusy;
print("Hello World");
"""
    st.markdown("# Page 1")
    st.markdown(mktext)
    st.code(code)


def main_page_function() -> None:
    st.title("Page 1")
    pic_func()
    mark_down_test()


# Execute Function
main_page_function()
