import streamlit as st
import logging
from rich.logging import RichHandler
import requests as rq

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)
log = logging.getLogger("rich")


def pic_func() -> None:
    st.image("https://picsum.photos/200")


def logo():
    url = "https://snips.sh/f/ahGYgGrGUK?r=1"
    url2 = "https://snips.sh/f/ahGYgGrGK?r=2"
    try:
        rez1 = rq.get(url)
        rez1.raise_for_status()  # This will raise an HTTPError for bad responses
        print(rez1.text)
    except rq.exceptions.HTTPError as http_err:
        log.error("HTTP error occurred: %s", http_err)
    except Exception as e:
        log.error("Other error occurred: %s", e)
