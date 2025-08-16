import streamlit as st
import pickle
import base64

model = pickle.load(open("spam_email_classifier.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


def add_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


add_bg_from_local("img.png")


st.markdown(
    """
    <div style='
        position: absolute left;
        top: 50%;
        left: 5%;
        transform: translateY(-50%);
    '>
        <h1 style='
            color: white;
            font-family: Arial;
            font-size: 48px;
        '>
             📧 Email Spam Detector
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)


email_text = st.text_area("Enter The Email Content:")

if st.button("Detect"): 
    input_vector = vectorizer.transform([email_text])
    prediction = model.predict(input_vector)[0]

    if prediction == 1:
        st.markdown(
            """
            <div style="background-color:#8B0000; padding:15px; border-radius:10px; color:white; font-size:18px;">
                 This email is <b>SPAM</b> 🚨
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="background-color:#006400; padding:15px; border-radius:10px; color:white; font-size:18px;">
                 This email is <b>NOT spam</b>
            </div>
            """,
            unsafe_allow_html=True
        )
