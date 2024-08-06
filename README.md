![Screenshot 2024-08-06 202809](https://github.com/user-attachments/assets/e2881edc-983f-4987-892e-af0a33f8d933)


# Spam Filter AI

Spam Filter AI is a Python application designed to classify emails as spam or non-spam using machine learning techniques. By utilizing Natural Language Processing (NLP) and Naive Bayes classification, this tool helps maintain an organized and spam-free inbox.

## 🚀 Project Overview

Spam Filter AI employs advanced machine learning methods to process and analyze email content, categorizing it as spam or non-spam. Key components include:

- **Natural Language Processing (NLP)**: For analyzing and understanding text.
- **Naive Bayes Classification**: For spam detection.
- **TF-IDF Vectorization**: To convert text into numerical features.

### Key Features

- **Direct Email Pasting**: Users can paste email content directly into the application.
- **Real-Time Classification**: Provides instant classification of email content.
- **Modern GUI**: Intuitive interface for ease of use.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## 🛠️ Technologies Used

- **Python**: Main programming language.
- **scikit-learn**: For machine learning algorithms and preprocessing.
- **tkinter**: For creating the graphical user interface.
- **pandas**: For data manipulation and analysis.
- **NLTK**: For text processing and NLP.

## 📥 Installation Guide

### Prerequisites

- **Python**: Version 3.7 or higher. Download from the [official Python website](https://www.python.org/downloads/).
- **Git**: For cloning the repository. Download from the [official Git website](https://git-scm.com/downloads).

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sd338/spam-filter-ai.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd spam-filter-ai
   ```

3. **Create and Activate a Virtual Environment**

   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

## 📂 Project Structure

- **`src/`**: Contains source code files.
  - `gui.py`: Manages the graphical user interface.
  - `model.py`: Handles model training and prediction.
  - `data_preprocessing.py`: Prepares and processes data.
  - `feature_extraction.py`: Extracts features from email content for the model.
  - `evaluation.py`: Evaluates model performance.
- **`data/`**: Directory for storing datasets.
- **`requirements.txt`**: Lists all dependencies.
- **`README.md`**: This file.
- **`LICENSE`**: License information.

## 📈 Usage Instructions

### Running the Application

- **Windows**:
  ```bash
  python src/gui.py
  ```

- **macOS/Linux**:
  ```bash
  python3 src/gui.py
  ```

### How to Use

1. **Paste Email Content**: Copy and paste email content into the text area in the GUI.
2. **Submit Email**: Click "Submit Email" to classify the content.
3. **Delete Mail**: Click "Delete Mail" to clear the text area.

## 📊 Data

Datasets are sourced from Kaggle. To obtain:

1. **Visit Kaggle**: Go to [Kaggle Datasets](https://www.kaggle.com/datasets).
2. **Search for Spam Datasets**: Use keywords like "spam email dataset."
3. **Download and Place in `data/` Directory**: Save the datasets here.

**Example Datasets:**
- [Spam Collection Dataset](https://www.kaggle.com/datasets)
- [Spam Emails Dataset](https://www.kaggle.com/datasets)

## 🤝 Contributing

Contributions are welcome! Here’s how to contribute:

1. **Fork the Repository**: Click "Fork" on GitHub.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/your-username/spam-filter-ai.git
   ```
3. **Create a New Branch**:
   ```bash
   git checkout -b feature-or-bugfix-name
   ```
4. **Make Changes**: Implement your features or fixes.
5. **Commit and Push**:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature-or-bugfix-name
   ```
6. **Submit a Pull Request**: Open a pull request on GitHub.

## 📝 License

This project is licensed under the GNU General Public License v3.0. The GPL-3.0 is a strong copyleft license that requires you to make the source code of the project available if you distribute or modify the software. For more details, visit the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) page.

### Permissions
- **Commercial Use**: Allowed
- **Modification**: Allowed
- **Distribution**: Allowed
- **Patent Use**: Allowed
- **Private Use**: Allowed

### Limitations
- **Liability**: No warranty is provided.
- **Warranty**: The software is provided "as-is."

### Conditions
- **License and Copyright Notice**: Must be included in all copies and substantial portions of the software.
- **State Changes**: Modified versions must also be licensed under GPL-3.0.
- **Disclose Source**: Source code must be made available when distributing binaries or modified versions.
- **Same License**: Modified versions must be distributed under GPL-3.0.

## 📧 Contact

For questions or support, please reach out via the contact methods on my [GitHub profile](https://github.com/sd338). Note that the email address provided in the GUI (`support@spamfilterai.com`) is fictional and used for demonstration purposes only.

