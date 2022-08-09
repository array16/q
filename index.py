import streamlit as st
import time

my_bar = st.progress(0)
for i in range(100):
    my_bar.progress(i + 1)
    time.sleep(0.01)

my_bar.empty()  # Remove the progress bar
st.success('hello welcome to arrayweb')
