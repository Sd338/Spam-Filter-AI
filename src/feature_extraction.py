from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib

def extract_features(texts):
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(max_features=3000)
    # Fit and transform the texts
    X = vectorizer.fit_transform(texts)
    return X, vectorizer

if __name__ == "__main__":
    # Load the preprocessed data
    df = pd.read_csv('data/preprocessed_emails.csv')
    
    # Extract features from the 'text' column
    X, vectorizer = extract_features(df['text'])
    
    # Save the vectorizer and feature matrix
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    joblib.dump(X, 'X_features.pkl')
    
    # Print the shape of the feature matrix
    print("Feature matrix shape:", X.shape)
