import streamlit as st
import pickle

# Load the vectorizer and model
with open('spam_classifier_model1.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

# Set up the Streamlit page
st.set_page_config(page_title="Spam Detector", page_icon="📩")
st.title("📩 Spam Message Classifier")
st.write("Enter a message and find out whether it's spam or not.")

# Input text area
message = st.text_area("Your Message", height=150)

# Prediction button
if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Transform and predict
        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)[0]

        if prediction == 0:
            st.error("🛑 This message is **SPAM**.")
        else:
            st.success("✅ This message is **HAM** (Not Spam).")
