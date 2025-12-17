import streamlit as st
import pandas as pd
from streamlit_carousel import carousel

test_items = [
    dict(
        title="Slide 1",
        text="A tree in the savannah",
        img="image1.png",
        link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819",
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master",
    ),
    dict(
        title="Slide 4",
        text="PANDAS",
        img="pandas.webp",
    ),
    dict(
        title="Slide 4",
        text="CAT",
        img="cat.jpg",
    ),
]



st.header("The App Store")
st.caption("Custom Streamlit apps to solve your usecase.")
st.logo("logo.png", size='small')

carousel(items=test_items)
st.button("Get Started", type='primary')
st.file_uploader("Upload your data here")

st.sidebar.header("Find Out more")
st.sidebar.write("Custom Streamlit apps to solve your usecase.")

st.sidebar.button("Button", type='primary')
st.sidebar.file_uploader("Upload your data here")
