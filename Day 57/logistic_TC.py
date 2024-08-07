#create a model with logistic regression and Bow for the text classification
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# sample data
reviews = [
    "I loved this movie, it was good",
    "the movie was boring",
    "excellent movie, actors done well",
    "it was a normal movie, nothing special"
]
# positive = 1, negative = 0, neutral = 2
labels = [1, 0, 1, 2]
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)
y = np.array(labels)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")

new_review = ["I really enjoyed the movie"]
new_review_vector = vectorizer.transform(new_review)
new_review_pred = model.predict(new_review_vector)

print(f"label of new review: {new_review_pred[0]}")
