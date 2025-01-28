#Text Data Preprocessing Lib
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle
import numpy as np

# function for appending stem words
words = []
classes = []
word_tag_list = []
ignore_words = ['?','!','.',',','s','m']

train_data_file= open('intents.json').read()
intents = json.loads(train_data_file)
    
def get_stem_words (words,ignore_words):
     # Add all words of patterns to list
    stem_words=[]
    for word in words:
        if word not in ignore_words:
            w = stemmer.stem(word.lower())
            stem_words.append(w)
    return stem_words
        
for intent in intents['intent']:
    for pattern in intent['pattern']:
        pattern_word = nltk.word_tokenize(pattern)
        words.extend(pattern_word)
        word_tag_list.append((pattern_word,intent['tag']))
        
    # Add all tags to the classes list
    if intent['tag'] not in classes:
        classes.append(intent['tag'])
        stem_words = get_stem_words(words,ignore_words)

print(stem_words)
print(word_tag_list[0])
print(classes)

training_data = []
number_of_tags = len(classes)
labels = [0]*number_of_tags
for word_tags in word_tag_list:
    bag_of_words= []
    pattern_words = word_tags[0]
    for word in pattern_words:
        index = pattern_words.index(word)
        word = stemmer.stem(word.lower())
        pattern_words[index] = word

    for word in stem_words:
        if word in pattern_words:
            bag_of_words.append(1)
        else:
            bag_of_words.append(0)
    
    print(bag_of_words)

    labels_encoding = list(labels)
    tag = word_tags[1]
    tag_index = classes.index(tag)
    labels_encoding[tag_index] = 1
    training_data.append([bag_of_words,labels_encoding])

print(training_data[0])

def preprocess_train_data (training_data):
    training_data = np.array(training_data,dtype = object)
    train_x = list(training_data[:,0])
    train_y = list(training_data[:,1])
    print(train_x[0])
    print(train_y[0])
    return train_x , train_y

train_x,train_y = preprocess_train_data(training_data)
#Create word corpus for chatbot

