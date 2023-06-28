import numpy as np
import streamlit as st
from predict import text_to_sequences, predict



st.title("Tweet Emotion Recognition")

st.write("Tweet Emotion Recognition can accurately identify a wide a range of emotions such as Suprise, Fear, Joy, Angry, Sadness and Love.")

tweet = st.text_area("Tweet Your Emotion", help="You can tweet about your Emotion.")

submit = st.button("Submit")

if submit:   
    st.title("Result")

    padded = text_to_sequences(tweet)

    a = predict(padded)


    st.write(a)
    