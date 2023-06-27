import pandas as pd
import pickle


MODEL_PATH = './models/tweet_model.pkl'


def predict(tweet):

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    # model = pd.read_pickle(MODEL_PATH)

    predicted = model.predict(tweet)
    print(predicted)



tweet = "i feel awful about it too because it s my job to get him in a position to succeed and it just didn t happen here"

predict(tweet)