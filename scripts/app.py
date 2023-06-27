import streamlit as st



st.title("Tweet Emotion Recognition")

st.write("Tweet Emotion Recognition can accurately identify a wide a range of emotions such as Suprise, Fear, Joy, Angry, Sadness and Love.")
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

text = st.text_area("Tweet About Emotion", help="You can tweet about your Emotion.")

submit = st.button("Submit")

if submit:
    st.write(text)