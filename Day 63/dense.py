import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample data
sentences = [
    "I love my bike!",
    "I had the worst experience in service.",
    "It was ok, but nothing special.",
    "The service consultant was terrible."
]

# Labels: Positive = 1, Negative = 0, Neutral = 2
labels = [1, 0, 2, 0]

# Tokenization and padding of sequences
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

# Convert sentences to sequences
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')

# Create the model
model = Sequential([
    Embedding(input_dim=10000, output_dim=64, input_length=padded.shape[1]),
    LSTM(64, return_sequences=False),
    Dropout(0.5),
    Dense(3, activation='softmax')
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(padded, np.array(labels), epochs=5, verbose=1)

# Make a prediction
test_sentences = ["I enjoyed the films."]
test_seq = tokenizer.texts_to_sequences(test_sentences)
test_padded = pad_sequences(test_seq, maxlen=padded.shape[1])
prediction = model.predict(test_padded)
predicted_class = np.argmax(prediction)

print(f"Predicted sentiment of the sentence: {predicted_class}")
