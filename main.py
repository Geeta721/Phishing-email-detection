
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.sparse import hstack, csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ============================================================
# 1. LOAD DATASET
# ============================================================

data = pd.read_csv("dataset/emails.csv")

# Remove empty rows
data = data.dropna(subset=["email", "label"])

emails = data["email"].astype(str)
labels = data["label"].astype(str)


# ============================================================
# 2. FEATURE EXTRACTION
# ============================================================

# ---------- Text features using TF-IDF ----------

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=3000
)

text_features = vectorizer.fit_transform(emails)


# ---------- URL feature ----------

def contains_url(text):
    return 1 if re.search(r"http[s]?://|www\.|\.com/|\.net/|\.org/", text.lower()) else 0


# ---------- Suspicious keyword feature ----------

suspicious_words = [
    "urgent",
    "verify",
    "verification",
    "password",
    "account",
    "suspended",
    "blocked",
    "click",
    "winner",
    "prize",
    "reward",
    "bank",
    "login",
    "confirm",
    "security",
    "immediately",
    "claim",
    "limited",
    "payment"
]


def suspicious_keyword_count(text):
    text = text.lower()

    count = 0

    for word in suspicious_words:
        if word in text:
            count += 1

    return count


# Create numerical features
url_features = emails.apply(contains_url).values.reshape(-1, 1)

keyword_features = emails.apply(
    suspicious_keyword_count
).values.reshape(-1, 1)


# Convert to sparse matrices
url_features = csr_matrix(url_features)
keyword_features = csr_matrix(keyword_features)


# Combine all features
features = hstack([
    text_features,
    url_features,
    keyword_features
])


# ============================================================
# 3. SPLIT DATA INTO TRAINING AND TESTING
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    features,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)


# ============================================================
# 4. CREATE MACHINE LEARNING MODEL
# ============================================================

model = LogisticRegression(
    max_iter=1000
)


# ============================================================
# 5. TRAIN MODEL
# ============================================================

model.fit(X_train, y_train)

print("\n==========================================")
print("   PHISHING EMAIL DETECTION MODEL")
print("==========================================")

print("\nModel trained successfully!")


# ============================================================
# 6. TEST MODEL
# ============================================================

predictions = model.predict(X_test)


# ============================================================
# 7. ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:", round(accuracy * 100, 2), "%")


# ============================================================
# 8. CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# ============================================================
# 9. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_test,
    predictions,
    labels=["Safe", "Phishing"]
)

print("\nConfusion Matrix:")
print(cm)


# Display confusion matrix
plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Safe", "Phishing"],
    yticklabels=["Safe", "Phishing"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Phishing Email Detection - Confusion Matrix")

plt.tight_layout()
plt.show()


# ============================================================
# 10. FUNCTION FOR NEW EMAIL
# ============================================================

def predict_email(email_text):

    # Convert new email into TF-IDF features
    new_text_features = vectorizer.transform(
        [email_text]
    )

    # URL feature
    new_url_feature = csr_matrix([
        [contains_url(email_text)]
    ])

    # Suspicious keyword feature
    new_keyword_feature = csr_matrix([
        [suspicious_keyword_count(email_text)]
    ])

    # Combine features
    new_features = hstack([
        new_text_features,
        new_url_feature,
        new_keyword_feature
    ])

    # Prediction
    prediction = model.predict(new_features)[0]

    # Probability
    probabilities = model.predict_proba(new_features)[0]

    # Find probability for predicted class
    class_index = list(model.classes_).index(prediction)

    confidence = probabilities[class_index] * 100

    return prediction, confidence


# ============================================================
# 11. TEST YOUR OWN EMAIL
# ============================================================

print("\n==========================================")
print("       EMAIL SECURITY CHECKER")
print("==========================================")

print("\nEnter an email message below.")
print("Type EXIT to stop the program.\n")


while True:

    user_email = input("Enter email: ")

    if user_email.upper() == "EXIT":
        print("\nProgram ended.")
        break

    prediction, confidence = predict_email(
        user_email
    )

    print("\n------------------------------------------")

    if prediction == "Phishing":
        print("Prediction : PHISHING")
        print("Warning    : This email may be suspicious.")

    else:
        print("Prediction : SAFE")
        print("Message    : No phishing pattern detected.")

    print("Confidence :", round(confidence, 2), "%")

    print("------------------------------------------\n")


