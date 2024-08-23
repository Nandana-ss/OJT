import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize
x_train, x_test = x_train / 255.0, x_test / 255.0

# Reshape the data for CNN
x_train_cnn = x_train.reshape(-1, 28, 28, 1)
x_test_cnn = x_test.reshape(-1, 28, 28, 1)

# One hot encoding for ANN and CNN
y_train_oh = to_categorical(y_train, 10)
y_test_oh = to_categorical(y_test, 10)

# Build an ANN model
ann_model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile and train the ANN model
ann_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
ann_model.fit(x_train, y_train_oh, epochs=5, batch_size=32, validation_data=(x_test, y_test_oh))

# Build a CNN model
cnn_model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile and train the CNN model
cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
cnn_model.fit(x_train_cnn, y_train_oh, epochs=5, batch_size=32, validation_data=(x_test_cnn, y_test_oh))

# Build the model with KNN
x_train_knn = x_train.reshape(-1, 28 * 28)
x_test_knn = x_test.reshape(-1, 28 * 28)

scaler = StandardScaler()
x_train_knn = scaler.fit_transform(x_train_knn)
x_test_knn = scaler.transform(x_test_knn)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(x_train_knn, y_train)

# Evaluate KNN model
knn_accuracy = knn_model.score(x_test_knn, y_test)
print("KNN accuracy: {:.2f}%".format(knn_accuracy * 100))


predictions = cnn_model.predict(x_test_cnn)

for i in range(5):
   plt.imshow(x_test[i], cmap = 'grey')
   plt.title(f"True: {y_test[i]},predicted: {np.argmax(predictions[i])}")
   plt.show()