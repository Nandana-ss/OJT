import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Sample data
data = [
    ("I love NLP", "positive"),
    ("I hate this technology", "negative"),
    ("It's ok, no worries", "neutral")
]

# Unpack sentences and labels
sentences, labels = zip(*data)

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Get stopwords
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

# Preprocess sentences
preprocessed_sentences = [preprocess(sentence) for sentence in sentences]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the sentences
x = vectorizer.fit_transform(preprocessed_sentences)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

# Initialize the classifier
classifier = MultinomialNB()

# Train the classifier
classifier.fit(x_train, y_train)

# Predict on the test set
y_pred = classifier.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Generate classification report
report = classification_report(y_test, y_pred)

# Print accuracy and classification report
print("Accuracy:", accuracy)
print("Classification Report:")
print(report)
