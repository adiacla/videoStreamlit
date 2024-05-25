"""
opencv-python-headless
streamlit
streamlit-webrtc
    
pip install -U streamlit streamlit-webrtc opencv-python-headless
pip install av

ERROR EN PC CON WINDOWS 11
https://www.whitphx.info/posts/20211231-streamlit-webrtc-video-app-tutorial/

opencv-python-headless
streamlit
streamlit-webrtc
av
"""

import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("Ejemplo video en Streaming usando Streamlit-webrtc")
st.write("Alfredo Diaz")


class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 200
        self.threshold2 = 200

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)
if ctx.video_processor:
    ctx.video_processor.threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
    ctx.video_processor.threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)