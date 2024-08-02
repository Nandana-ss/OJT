import tensorflow as tf
from tensorflow.keras import backend as K
import numpy as np
def weighted_mse(y_true, y_pred, weights):
    """
    Custom weighted mean squared error loss function.
    
    Parameters:
    y_true -- true labels
    y_pred -- predicted labels
    weights -- weights for each sample in the batch
    
    Returns:
    Weighted MSE loss value
    """
    # Compute the squared differences between true and predicted labels
    squared_diff = tf.square(y_true - y_pred)
    # Multiply the squared differences by the weights
    weighted_squared_diff = squared_diff * weights
    # Return the mean of the weighted squared differences
    return K.mean(weighted_squared_diff, axis=-1)

# Usage in a model
# Assume `weights` is a tensor of shape (batch_size,)
weights = tf.constant([1.0, 2.0, 0.5, 1.5]) 
# Create a model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1)
])

# Compile the model with the custom loss function
model.compile(optimizer='adam', loss=lambda y_true, y_pred: weighted_mse(y_true, y_pred, weights))

X_train = np.random.rand(4, 10)
y_train = np.random.rand(4, 1)

# Train the model
model.fit(X_train, y_train, epochs=10)
