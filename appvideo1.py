"""
opencv-python-headless
streamlit
streamlit-webrtc
    
pip install -U streamlit streamlit-webrtc opencv-python-headless
    
"""

import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("My first Streamlit app")
st.write("Hello, world")

webrtc_streamer(key="example")