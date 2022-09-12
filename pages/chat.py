import streamlit as st
from streamlit_discourse import st_discourse

st.title("Chat With Others")


discourse_url = "discuss.streamlit.io"
topic_id = 1726

st_discourse(discourse_url, topic_id)