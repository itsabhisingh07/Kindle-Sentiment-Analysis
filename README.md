#  Kindle Review Sentiment Analyzer

A Machine Learning web application that predicts the sentiment of book reviews (Positive or Negative). Built with **Python**, **Flask**, and **Scikit-Learn** using a **Random Forest** classifier trained on TF-IDF vectors.

##  Overview
- **Input:** A user enters a text review (e.g., "The plot was amazing but the characters were dull.").
- **Process:** The app cleans the text (removes stopwords, lemmatization), converts it to numbers using TF-IDF, and feeds it to the model.
- **Output:** The model predicts whether the sentiment is **Positive**  or **Negative** .

##  Project Structure
```text
Kindle_Sentiment_App/
│
├── model.pkl               # Trained Random Forest Model
├── vectorizer.pkl          # TF-IDF Vectorizer
├── app.py                  # Flask Application
├── requirements.txt        # Dependencies
│
├── static/
│   └── style.css           # Styling for the website
│
└── templates/
    └── index.html          # HTML Interface

