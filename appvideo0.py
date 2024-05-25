"""
opencv-python-headless
streamlit
streamlit-webrtc
    
pip install -U streamlit streamlit-webrtc opencv-python-headless
pip install av

ERROR EN PC CON WINDOWS 11
https://www.whitphx.info/posts/20211231-streamlit-webrtc-video-app-tutorial/
"""

import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

st.title("Ejemplo video en Streaming usando Streamlit-webrtc")
st.write("Alfredo Diaz")


class VideoProcessor:
    def __init__(self) -> None:
        pass

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # No se aplica ningún procesamiento a la imagen
        return av.VideoFrame.from_ndarray(img, format="bgr24")


ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)