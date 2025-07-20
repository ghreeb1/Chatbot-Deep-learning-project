
# 🧠 Psychologist Chatbot - Deep Learning Project

A deep learning-based chatbot designed to simulate supportive psychological conversations. Built using Python, TensorFlow/Keras, and Flask, the bot offers a simple web interface and customizable training data.

---

## 📁 Project Structure

```
Chatbot-Deep-learning-project/
├── templates/
│   └── 7.png, 8.png                  # UI and training screenshots
├── Psychologist.h5                   # Trained Keras model
├── app.py                            # Flask web app
├── classes.pkl                       # Pickled class labels
├── intents.json                      # Conversation training data
├── t.py                              # (Utility script - clarify use)
├── train.ipynb                       # Model training notebook
└── words.pkl                         # Pickled vocabulary
```

---

## 🖼️ Screenshots

**Chat Interface**  
![Chatbot Interface](https://github.com/ghreeb1/Chatbot-Deep-learning-project/blob/master/templates/7.png)

**Model Training**  
![Training Process](https://github.com/ghreeb1/Chatbot-Deep-learning-project/blob/master/templates/8.png)

---

## 🚀 Features

- 🗣️ Psychological conversation patterns using NLP
- 🤖 Deep learning with TensorFlow/Keras
- 🌐 Flask-based web interface
- 🔧 Easy to update with new training data (`intents.json`)
- 💬 Supports basic empathetic interactions

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ghreeb1/Chatbot-Deep-learning-project.git
   cd Chatbot-Deep-learning-project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the chatbot:
   ```bash
   python app.py
   ```
   Access the chatbot at: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Training the Model

To customize or retrain the chatbot:

1. Edit the `intents.json` file with new intents and responses.
2. Open and run the notebook:
   ```bash
   jupyter notebook train.ipynb
   ```

This will retrain the model and regenerate `Psychologist.h5`.

---

## 📦 Dependencies

- Python 3.6+
- TensorFlow 2.x
- Flask
- NLTK
- NumPy
- Pickle

---

## 🧠 Example Intents (from `intents.json`)
```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey there"],
      "responses": ["Hello, how can I help you today?", "Hi! How are you feeling?"]
    },
    {
      "tag": "anxiety",
      "patterns": ["I feel anxious", "I have anxiety", "I'm worried"],
      "responses": ["I'm sorry to hear that. Do you want to talk more about it?", "Anxiety is tough. You're not alone."]
    }
  ]
}
```

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by open-source chatbot architectures
- Thanks to contributors and supporters of open mental health technology

---

## 🔧 Future Improvements

- [ ] Add LSTM or transformer-based contextual layers
- [ ] Integrate sentiment analysis
- [ ] Add logging and analytics
- [ ] Multi-language support
- [ ] User authentication & chat history

---

## 🔍 Notes

> If image links are broken, verify that the GitHub repository is **public** and that the URLs are in this format:
> ```
> https://github.com/ghreeb1/Chatbot-Deep-learning-project/blob/master/templates/7.png
> ```
## 📧 Contact

**Developer:**  
Mohamed Khaled

**Email:**  
qq11gharipqq11@gmail.com

**Project Link:**  
[https://github.com/ghreeb1/Eye_Disease.Classification](https://github.com/ghreeb1/Eye_Disease.Classification)

**LinkedIn:**  
[https://linkedin.com/in/mohamed-khaled-3a9021263](https://linkedin.com/in/mohamed-khaled-3a9021263)
