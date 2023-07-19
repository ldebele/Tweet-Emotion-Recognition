# import numpy as np
import streamlit as st
from predict import text_to_sequences, predict



st.title("Tweet Emotion Recognition")

st.write("The objective of this project is to recognize a broad range of emotions. It has the ability to identify emotions like Surprise, Fear, Joy, Anger, Sadness, and Love. The model can effectively analyze and classify emotional expressions present in tweet texts.")
tweet = st.text_area("Tweet Your Emotion", help="You can tweet about your Emotion.")

submit = st.button("Tweet")

Emotions = {
    "Surprise": ":astonished:",
    "Fear": ":fearful:",
    "Joy": ":smile:",
    "Anger": ":angry:",
    "Sadness": ":cry:",
    "Love": ":heart:"
}

if submit:
    # generate padded and sequence of the tweet   
    padded = text_to_sequences(tweet)
    # predict the tweet
    emotion = predict(padded)
    
    st.subheader("Result")
    st.markdown(f'**Emotion** :  {emotion} {Emotions[emotion]}')
    