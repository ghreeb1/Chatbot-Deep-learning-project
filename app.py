import random
import numpy as np
import pickle
import json
from flask import Flask, render_template, request, redirect, url_for
from flask_ngrok import run_with_ngrok
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

model = load_model("Psychologist.h5")
data_file = open("intents.json").read()
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
        print("Received message:", msg) 
        intents = json.loads(data_file)
        if msg.startswith('my name is'):
            name = msg[11:]
            ints = predict_class(msg, model)
            res1 = getResponse(ints, intents)
            res = res1.replace("{n}", name)
        elif msg.startswith('hi my name is'):
            name = msg[14:]
            ints = predict_class(msg, model)
            res1 = getResponse(ints, intents)
            res = res1.replace("{n}", name)
        else:
            ints = predict_class(msg, model)
            res = getResponse(ints, intents)
        print("Response:", res)  
        return res
    return render_template("chat.html")

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get('msg')
    print("Received message:", user_msg)  
    intents = json.loads(data_file)
    if user_msg.startswith('my name is'):
        name = user_msg[11:]
        ints = predict_class(user_msg, model)
        res1 = getResponse(ints, intents)
        res = res1.replace("{n}", name)
    elif user_msg.startswith('hi my name is'):
        name = user_msg[14:]
        ints = predict_class(user_msg, model)
        res1 = getResponse(ints, intents)
        res = res1.replace("{n}", name)
    else:
        ints = predict_class(user_msg, model)
        res = getResponse(ints, intents)
    print("Response:", res) 
    return res

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result

if __name__ == "__main__":
    app.run()
