import json
import os
import time

import streamlit as st

from lecture_log import lecture_log

L = lecture_log()

debut_message = ""

st.sidebar.image("./data_streamlit/bdf.png")

st.title("My demo")


@st.cache(allow_output_mutation=True)
def my_sleep():
    time.sleep(3)


my_sleep()

log_option = st.sidebar.selectbox(
    "Select your logs", ["Select trace", "Select warning", "Select error"]
)

if log_option == "Select trace":
    result = L.lecture_trace(with_print=False)
    with st.beta_expander("Expand"):
        st.image("./data_streamlit/bdf.png")

elif log_option == "Select warning":
    result = L.lecture_warning(with_print=False)
    st.sidebar.radio("Radio", ["Paul", 2, 3])
elif log_option == "Select error":
    result = L.lecture_error(with_print=False)

st.date_input("Date input")

st.write(json.dumps(result))
