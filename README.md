# 📧 Phishing Email Detection Model

## 📌 Project Overview

The **Phishing Email Detection Model** is a machine learning-based cybersecurity project that classifies emails as either **Phishing** or **Safe**.

The project uses **Scikit-learn** to train a classification model on labelled email data. It analyzes the textual content of emails and extracts additional features such as **URLs and suspicious keywords** to identify potential phishing messages.

---

## 🎯 Objectives

* Detect phishing emails using machine learning.
* Classify emails as **Phishing** or **Safe**.
* Extract useful features from email content.
* Analyze URLs and suspicious keywords.
* Display model accuracy.
* Generate a confusion matrix for model evaluation.
* Allow users to enter their own email for prediction.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Dataset handling
* **Scikit-learn** – Machine learning
* **TF-IDF** – Text feature extraction
* **Logistic Regression** – Classification algorithm
* **Matplotlib** – Visualization
* **Seaborn** – Confusion matrix visualization
* **Regular Expressions (Regex)** – URL detection

---

## 📂 Project Structure

```text
Phishing-Email-Detection/
│
├── dataset/
│   └── emails.csv
│
├── main.py
│
└── README.md
```

---

## ⚙️ How the System Works

```text
              Email Dataset
                    │
                    ▼
            Data Preprocessing
                    │
                    ▼
              Feature Extraction
             ┌──────┴───────┐
             │              │
          TF-IDF       URL/Keyword
             │              │
             └──────┬───────┘
                    ▼
             Feature Combination
                    │
                    ▼
            Logistic Regression
                    │
                    ▼
             Model Prediction
              ┌─────┴─────┐
              ▼           ▼
          Phishing       Safe
                    │
                    ▼
          Accuracy + Confusion Matrix
```

---

## 🔍 Features

### 1. TF-IDF Text Analysis

The email text is converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

This helps the model identify words and patterns that may be useful for distinguishing phishing emails from legitimate emails.

### 2. URL Detection

The system checks whether an email contains URLs such as:

```text
http://
https://
www.
.com/
.net/
.org/
```

### 3. Suspicious Keyword Detection

The system checks for potentially suspicious terms such as:

```text
urgent
verify
password
account
blocked
click
winner
prize
bank
login
confirm
security
immediately
claim
```

### 4. Machine Learning Classification

The project uses **Logistic Regression** to classify emails into:

```text
Phishing
Safe
```

### 5. Model Evaluation

The model calculates:

* Accuracy
* Classification report
* Confusion matrix

---

## 🚀 Installation

Make sure Python is installed.

Install the required libraries using:

```bash
python -m pip install pandas scikit-learn matplotlib seaborn
```

---

## ▶️ How to Run

Open the project in Python IDLE or another Python editor.

Run:

```text
main.py
```

The program will:

1. Load the email dataset.
2. Extract text features.
3. Extract URL and suspicious keyword features.
4. Split the dataset into training and testing data.
5. Train the Logistic Regression model.
6. Calculate accuracy.
7. Display the confusion matrix.
8. Allow the user to enter an email.
9. Predict whether the email is **Phishing** or **Safe**.

---

## 🧪 Example

### Input

```text
URGENT! Your bank account has been suspended.
Click here immediately to verify your password.
```

### Output

```text
Prediction : PHISHING
Warning    : This email may be suspicious.
```

### Safe Email Example

```text
Hello, our project meeting is scheduled for tomorrow
at 10 AM. Please bring the assignment documents.
```

### Output

```text
Prediction : SAFE
Message    : No phishing pattern detected.
```

---

## 📊 Evaluation

The model is evaluated using a **confusion matrix**.

The confusion matrix shows:

* Correctly classified Safe emails
* Correctly classified Phishing emails
* Safe emails incorrectly classified as Phishing
* Phishing emails incorrectly classified as Safe

Accuracy is also calculated to measure the overall percentage of correct predictions on the test set.

---

## 🔐 Cybersecurity Relevance

Phishing is a common social engineering technique used to trick users into revealing sensitive information such as:

* Passwords
* Banking information
* Login credentials
* Personal information

Automated phishing detection can help identify suspicious messages before users interact with them.

---

## ⚠️ Limitations

This project is a **prototype for educational purposes**.

The initial dataset is relatively small, so the accuracy obtained from it should not be considered representative of real-world phishing detection performance.

A production-ready system would require:

* A much larger dataset
* More diverse phishing examples
* Legitimate emails from different sources
* More advanced URL analysis
* Sender and header analysis
* Attachment analysis
* Continuous model evaluation

---

## 🔮 Future Enhancements

Possible improvements include:

* Use a larger real-world email dataset.
* Add sender address analysis.
* Analyze email headers.
* Detect suspicious domains.
* Check URL reputation.
* Add attachment analysis.
* Experiment with Random Forest and other classifiers.
* Create a graphical user interface.
* Deploy the model as a web application.
* Add real-time email scanning.

---

## 👩‍💻 Author

**Geethalakshmi**

Cybersecurity Student

---

## 📜 Disclaimer

This project is developed for **educational and cybersecurity learning purposes**. It should not be considered a complete replacement for professional email security systems.
