import sys
import os
import tkinter as tk
from tkinter import messagebox
import joblib  # Correct import for joblib

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the preprocess_text function from data_preprocessing
from src.data_preprocessing import preprocess_text

class SpamFilterAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spam Filter AI")
        self.root.geometry("600x500")
        self.root.configure(bg='#F2F2F2')

        # Header
        header = tk.Frame(self.root, bg='#4A90E2', pady=10)
        header.pack(fill='x')
        title = tk.Label(header, text="Spam Filter AI", font=("Roboto", 24, "bold"), fg='#FFFFFF', bg='#4A90E2')
        title.pack()

        # Main content area
        content = tk.Frame(self.root, bg='#F2F2F2', padx=20, pady=20)
        content.pack(fill='both', expand=True)

        # Instructions
        instructions = tk.Label(content, text="Paste the email content below:", font=("Roboto", 12), bg='#F2F2F2', fg='#333333')
        instructions.pack(pady=10)

        # Email Content Text Area
        self.email_text = tk.Text(content, height=10, width=70, wrap='word', bg='#FFFFFF', fg='#333333', font=("Roboto", 12))
        self.email_text.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(content, bg='#F2F2F2')
        button_frame.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(button_frame, text="Submit Email", command=self.process_email, font=("Roboto", 14), bg='#50E3C2', fg='#FFFFFF', relief='flat', padx=10, pady=5)
        self.submit_button.grid(row=0, column=0, padx=10)

        # Delete Mail Button
        self.delete_button = tk.Button(button_frame, text="Delete Mail", command=self.delete_mail, font=("Roboto", 14), bg='#E94E77', fg='#FFFFFF', relief='flat', padx=10, pady=5)
        self.delete_button.grid(row=0, column=1, padx=10)

        # Status Label
        self.status_label = tk.Label(content, text="Paste an email and click Submit to check.", font=("Roboto", 12), bg='#F2F2F2', fg='#333333')
        self.status_label.pack(pady=10)

        # Footer
        footer = tk.Frame(self.root, bg='#4A90E2', pady=10)
        footer.pack(side='bottom', fill='x')
        footer_text = tk.Label(footer, text="© 2024 Spam Filter AI | Contact: support@spamfilterai.com", font=("Roboto", 10), fg='#FFFFFF', bg='#4A90E2')
        footer_text.pack()

        # Load the model and vectorizer
        self.model = joblib.load('spam_detector_model.pkl')
        self.vectorizer = joblib.load('tfidf_vectorizer.pkl')

    def process_email(self):
        email_content = self.email_text.get("1.0", tk.END).strip()
        if email_content:
            preprocessed_content = preprocess_text(email_content)
            features = self.vectorizer.transform([preprocessed_content])
            prediction = self.model.predict(features)

            if prediction == 1:
                result_text = "This email is SPAM."
            else:
                result_text = "This email is NOT spam."

            self.status_label.config(text=result_text)
        else:
            messagebox.showwarning("Empty Content", "Please paste an email into the text area before submitting.")

    def delete_mail(self):
        self.email_text.delete("1.0", tk.END)
        self.status_label.config(text="Paste an email and click Submit to check.")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = SpamFilterAIApp(root)
    root.mainloop()
