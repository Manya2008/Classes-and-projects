import pandas as pd
import numpy as np

import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
# train data
train_data = pd.read_csv("static/data_files/tweet_emotions.csv")    
training_sentences = []

for i in range(len(train_data)):
    sentence = train_data.loc[i, "content"]
    training_sentences.append(sentence)

#load model
model = load_model("static/model_files/Tweet_Emotion.h5")

vocab_size = 40000
max_length = 100
trunc_type = "post"
padding_type = "post"
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

#assign emoticons for different emotions
emo_code_url = {
    "empty": [0, "./static/assets/emoticons/Empty.png"],
    "sadness": [1,"./static/assets/emoticons/Sadness.png" ],
    "enthusiasm": [2, "./static/assets/emoticons/Enthusiasm.png"],
    "neutral": [3, "./static/assets/emoticons/Neutral.png"],
    "worry": [4, "./static/assets/emoticons/Worry.png"],
    "surprise": [5, "./static/assets/emoticons/Surprise.png"],
    "love": [6, "./static/assets/emoticons/Love.png"],
    "fun": [7, "./static/assets/emoticons/fun.png"],
    "hate": [8, "./static/assets/emoticons/hate.png"],
    "happiness": [9, "./static/assets/emoticons/happiness.png"],
    "boredom": [10, "./static/assets/emoticons/boredom.png"],
    "relief": [11, "./static/assets/emoticons/relief.png"],
    "anger": [12, "./static/assets/emoticons/anger.png"]
    
    }
# write the function to predict emotion
def predict (text):
    predicted_emotion = ""
    predicted_emotion_img_url = ""
    if text != "":
        sentance = []
        sentance.append(text)
        sequences = tokenizer.text_to_sequence(sentance)
        padded = pad_sequences(sequences,maxlen = max_length, padding = padding_type, truncating = trunc_type)
        testing_padded= np.array(padded)
        predicted_class_label = np.argmax(model.predict(testing_padded),axis=1)
        print(predicted_class_label)
        for key,value in emo_code_url.items():
            if value[0] == predicted_class_label:
                predicted_emotion_img_url = value[1]
                predicted_emotion = key
        return predicted_emotion,predicted_emotion_img_url

