import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from logger import logger
import numpy as np

encoded_labels = {
    'Amazonian Blue': 0,
    'Antipodean Opaleye': 1,
    'Canadian Sailwing': 2,
    'Chinese Fireball': 3,
    'Common Welsh Green': 4,
    'Egyptian Copperbelly': 5,
    'Hebridean Black': 6,
    'Hungarian Horntail': 7,
    'Kenyan Brushtail': 8,
    'Norwegian Ridgeback': 9,
    'Peruvian Vipertooth': 10,
    'Swedish Short Snout': 11,
    'Ukrainian Ironbelly': 12
}

reverse_labels = {v: k for k, v in encoded_labels.items()}

class NeuralNetworkClassifier:
    """Neural Network classifier for dragon species"""
    def __init__(self):
        self.model = None
        self.num_classes = len(encoded_labels)
        self.history = None

    def build_model(self, input_shape):
        """
        Build the neural network architecture
        :params: input_shape
        "returns: model
        """
        logger.info('Building neural network model...')
        model = Sequential([
            # Input layer
            Dense(32, activation='relu', input_shape=(input_shape,)),
            BatchNormalization(),
            Dropout(0.4),

            # Hidden layers
            Dense(64, activation='relu'),
            BatchNormalization(),
            Dropout(0.45),

            Dense(32, activation='relu'),
            BatchNormalization(),
            Dropout(0.5),

            # Output layer
            Dense(self.num_classes, activation='softmax')
        ])

        # Compile the model
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        logger.info('Build complete')

        self.model = model
        return model

    def fit(self, X_train, y_train, X_val=None, y_val=None, epochs=25, batch_size=32):
        """Train the neural network"""
        # Prepare validation data if provided
        validation_data = None
        if X_val is not None and y_val is not None:
            validation_data = (X_val, y_val)

        # Early stopping to prevent overfitting
        early_stopping = EarlyStopping(
            monitor='val_loss' if validation_data else 'loss',
            patience=10,
            restore_best_weights=True
        )

        # Train the model
        self.history = self.model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=validation_data,
            callbacks=[early_stopping],
            verbose=1
        )

        return self

    def predict(self, X):
        y_proba = self.model.predict(X)

        # Return class with highest probability
        return np.argmax(y_proba, axis=1)

    def evaluate(self, X, y):
        loss, accuracy = self.model.evaluate(X, y, verbose=0)
        return loss, accuracy

