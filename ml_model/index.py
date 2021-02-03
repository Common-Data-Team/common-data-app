# -*- coding:utf-8 -*-
import json

from sklearn.metrics import mean_squared_error
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pymorphy2
import pandas as pd
import pickle
import jsonlines
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.metrics.pairwise import linear_kernel
from gensim.models import word2vec
from tensorflow import keras
import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, Input
from keras.preprocessing.text import Tokenizer
from keras import regularizers
from keras.wrappers.scikit_learn import KerasClassifier
from keras import backend as K

def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))

morph = pymorphy2.MorphAnalyzer()

stops = set(stopwords.words("english")) | set(stopwords.words("russian"))
def review_to_wordlist(review: str) -> list:
    #1)
    review_text = re.sub("[^а-яА-Яa-zA-Z1-9]"," ", review)
    #2)
    words = review_text.lower().split()
    #3)
    words = [w for w in words if not w in stops]
    #4)
    words = [morph.parse(w)[0].normal_form for w in words ]
    return(words)

def type_to_encode(type_data: str) -> int:
    if type_data == "ShortText":
        return 0
    if type_data == "OneChoice":
        return 1
    if type_data == "MultipleChoice":
        return 2

class mean_vectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.dim = len(next(iter(w2v.values())))

    def fit(self, X):
        return self 

    def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec] 
                    or [np.zeros(self.dim)], axis=0)
            for words in X
        ])

def get_output(question: str, question_type: str) -> int:
    encoded_text = review_to_wordlist(question)
    encoded_type = type_to_encode(question_type)

    model = word2vec.Word2Vec.load('w2v')
    w2v = dict(zip(model.wv.index2word, model.wv.vectors))

    estimator = keras.models.load_model('model', 
                                        custom_objects={"f1_m": f1_m, 
                                                        "precision_m": precision_m, 
                                                        "recall_m": recall_m})
    
    data_mean = mean_vectorizer(w2v).fit([encoded_text]).transform([encoded_text])
    data_mean = np.concatenate((np.array([[encoded_type]]), data_mean), axis=1)

    return estimator.predict(data_mean)[0][0]
    
def handler(event, context):
	data = json.dumps(event)
	return {"label": get_output(data['question'], data['type'])}