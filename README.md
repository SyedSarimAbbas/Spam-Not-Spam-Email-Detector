***📧 Email Spam Detector***

A Streamlit-powered web application that detects whether an email is Spam or Not Spam using a Machine Learning model. The app is designed to be lightweight, user-friendly, and deployment-ready, making it an excellent project for machine learning, text classification, and interactive ML app development.

🔹 Features

Machine Learning model for spam classification

Interactive Streamlit interface

Dynamic text input box (auto-adjustable)

Styled prediction results (green = safe, red = spam)

Probability score for model confidence

Lightweight and deployable on Streamlit Cloud or Heroku

🔹 Tech Stack

Python

Scikit-learn (model training)

Streamlit (frontend interface)

Pickle (model & vectorizer storage)

🔹 About the Dataset

The model is trained on a publicly available spam/ham email dataset, commonly used for text classification research. The dataset contains labeled examples of spam (advertisements, promotions, scams) and ham (legitimate) emails, allowing the model to learn patterns in word usage, frequency, and context for accurate classification.


Run the app:

streamlit run app.py

🔹 Usage

Enter/paste an email in the text box.

Click Detect to classify the email.

View results with styled feedback + probability score.

🔹 Deployment

Easily deploy on Streamlit Cloud or Heroku for instant access.

 Email Spam Detector – A simple yet professional tool to classify emails and demonstrate real-world ML applications.
