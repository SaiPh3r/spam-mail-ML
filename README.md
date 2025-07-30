# 📩 Spam Mail Classifier - ML Web App

A simple Streamlit web application that classifies user-input messages as **Spam** or **Ham (Not Spam)** using a trained machine learning model based on TF-IDF and logistic regression.

🔗 **Live App**: [Click here to try it](https://saiph3r-spam-mail-ml-app-frwl0i.streamlit.app/)  
📂 **Dataset**: [Download from Google Drive](https://drive.google.com/file/d/1uzbhec5TW_OjFr4UUZkoMm0rpyvYdhZw/view)

---

## 🧠 How It Works

- The app uses a **TfidfVectorizer** to convert messages into numerical features.
- A **Logistic Regression model** trained on the dataset predicts whether the message is spam.
- Both the vectorizer and model are saved in a single `spam_classifier_model1.pkl` file.

---

## 🚀 Features

- 💬 Message input box
- ⚡ Real-time spam prediction
- 🧠 ML model powered by scikit-learn
- 🌐 Deployed on Streamlit Cloud

---

## 🛠️ Installation (For Local Run)

```bash
git clone https://github.com/yourusername/spam-mail-ml-app.git
cd spam-mail-ml-app
pip install -r requirements.txt
streamlit run spam_app.py
