import json
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


MODEL_DIR = './models/tweet_model.h5'
LABEL_DIR = './models/Labels.json'
TOKENIZER_DIR = './models/tokenizer_data.json'


def text_to_sequences(tweet):
    """
        params:
            tweet: str      -> raw string of the tweet
        
        return:
            padded: list    -> sequences and padded of the tweet
    """

    with open(TOKENIZER_DIR, 'r') as f:
        tokenizer_data = json.load(f)

    # parameters
    params = tokenizer_data['tokenizer_params']
    # Instiantiate the Tokenizer
    tokenizer = Tokenizer(num_words=params['num_words'], oov_token=params['oov_token'])

    # extract word_index from json
    word_index = tokenizer_data['word_index']

    # assign word index to the tokenizer
    tokenizer.word_index = word_index

    # generate and padded the sequences
    sequence = tokenizer.texts_to_sequences([tweet])
    padded = pad_sequences(sequence, maxlen=params['max_length'], padding=params['padding_type'], truncating=params['trunc_type'])

    return padded




def predict(padded_tweet):
    """
        params:
            padded_tweet: list
        
        return:
            emotion: str
    """

    # Load the saved model
    model = load_model(MODEL_DIR)

    # predict the tweet 
    predicted = model.predict(padded_tweet)

    # return the maximum index
    index = np.argmax(predicted)

    # open the json file
    with open(LABEL_DIR, 'r') as f:
        label = json.load(f)

    # get the emotions from the index
    emotion = label[str(index)]

    return emotion
