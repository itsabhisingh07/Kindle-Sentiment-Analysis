from flask import Flask, render_template, request
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)


model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    
    text = text.lower()
    
    
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'<.*?>', '', text)
    
    
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    
    text = " ".join(text.split())

    
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return " ".join(filtered_words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        
      
        cleaned_review = clean_text(review)
        
        
        vectorized_review = vectorizer.transform([cleaned_review]).toarray()
        
    
        probabilities = model.predict_proba(vectorized_review)[0]
        positive_confidence = probabilities[1] 
        
        threshold = 0.90  
        
        if positive_confidence > threshold:
            sentiment = "Positive "
            css_class = "positive"
        else:
            sentiment = "Negative "
            css_class = "negative"
            
        
        print(f"Review: {review[:30]}... | Confidence: {positive_confidence:.2f}")

      
            
        return render_template('index.html', prediction=sentiment, original_text=review, css_class=css_class)

if __name__ == '__main__':
    app.run(debug=True)