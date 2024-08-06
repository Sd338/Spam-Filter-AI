import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk

# Download stopwords if not already downloaded
nltk.download('stopwords')

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', ' ', text)  # Remove HTML tags
    text = re.sub(r'\d+', ' ', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', ' ', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    
    stop_words = set(stopwords.words('english'))
    stemmer = SnowballStemmer('english')
    
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    
    return ' '.join(tokens)

def preprocess_data(df, text_column):
    df[text_column] = df[text_column].apply(preprocess_text)
    return df

if __name__ == "__main__":
    # Load and check columns of emails.csv
    emails_df = load_data('data/emails.csv')
    print("Columns in emails.csv:", emails_df.columns)

    # Load and check columns of email.csv
    email_df = load_data('data/email.csv')
    print("Columns in email.csv:", email_df.columns)
    
    # Preprocess the data
    emails_df = preprocess_data(emails_df, 'text')  # Use 'text' as the column name for email content
    
    # Save the preprocessed data
    emails_df.to_csv('data/preprocessed_emails.csv', index=False)
    
    # Verify the number of rows processed
    print("Number of rows processed:", len(emails_df))
    print("Preprocessed DataFrame:")
    print(emails_df.head())
