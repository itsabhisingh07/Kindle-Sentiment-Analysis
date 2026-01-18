#  Kindle Review Sentiment Analyzer

A Machine Learning web application that predicts the sentiment of book reviews (Positive or Negative). Built with **Python**, **Flask**, and **Scikit-Learn** using a **Random Forest** classifier trained on TF-IDF vectors.

##  Overview
- **Input:** A user enters a text review (e.g., "The plot was amazing but the characters were dull.").
- **Process:** The app cleans the text (removes stopwords, lemmatization), converts it to numbers using TF-IDF, and feeds it to the model.
- **Output:** The model predicts whether the sentiment is **Positive**  or **Negative** .

##  Model Details
The sentiment analysis model is built using a supervised machine learning approach.
- **Algorithm:** Random Forest Classifier (`sklearn.ensemble.RandomForestClassifier`)
- **Feature Extraction:** TF-IDF Vectorizer (`sklearn.feature_extraction.text.TfidfVectorizer`)
- **Performance:** Achieved an accuracy of approximately **79.6%** on the test dataset.
- **Preprocessing Pipeline:**
  1. **Text Cleaning:** Removal of HTML tags, URLs, special characters, and numbers.
  2. **Tokenization:** Splitting text into individual words.
  3. **Stopword Removal:** Filtering out common English words (e.g., "the", "is") using NLTK.
  4. **Lemmatization:** Reducing words to their base form (e.g., "running" -> "run") using WordNetLemmatizer.

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


##  How to Run Locally

### 1. Clone the Repository
Open your terminal and run:

```bash
git clone [https://github.com/YOUR_USERNAME/Kindle-Sentiment-App.git](https://github.com/YOUR_USERNAME/Kindle-Sentiment-App.git)
cd Kindle-Sentiment-App

## Install Dependencies

```bash
!pip install -r requirements.txt
```
```bash
python app.py
```