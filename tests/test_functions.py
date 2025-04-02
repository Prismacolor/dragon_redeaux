import pytest
import numpy as np
import pandas as pd
import os
from unittest.mock import patch, MagicMock

from utils.helper import preprocess_data, numerical_labels_to_categories


# Mock for neural network model
class MockNeuralNetwork:
    def predict(self, X):
        # Mock prediction for testing
        return np.array([0, 1, 2])


# Fixtures
@pytest.fixture
def sample_data():
    """Create sample data for testing"""
    data = {
        'gender': ['male', 'female', 'male'],
        'estimated_age': ['juvenile', 'adult', 'elder'],
        'color_of_scales': ['blue', 'grey', 'green'],
        'color_of_eyes': ['red', 'yellow', 'multicolored'],
        'color_of_wings': ['grey', 'blue', 'purple'],
        'est_body_length': [3.5, 5.2, 4.7],
        'shape_of_snout': ['snub', 'long', 'snub'],
        'shape_of_teeth': ['pointed', 'serrated', 'pointed'],
        'scales_present': ['partial', 'yes', 'no'],
        'scale_texture': ['smooth', 'rough', 'smooth'],
        'body_texture': ['scaled', 'scaled', 'scaled'],
        'snout_length': [0.8, 1.2, 0.9],
        'shape_of_body': ['lithe', 'muscular', 'lithe'],
        'wingspan': [7.2, 10.5, 8.9],
        'number_of_limbs': [2, 4, 2],
        'facial_spikes': ['yes', 'no', 'yes'],
        'frilled': ['yes', 'yes', 'no'],
        'length_of_horns': ['long', 'medium', 'short'],
        'shape_of_horns': ['spiny', 'pointed', 'twisted'],
        'shape_of_tail': ['fluted', 'pointed', 'fluted'],
        'loc_of_sighting': ['Brazil', 'Peru', 'open ocean'],
        'aggressiveness': [4, 6, 3],
        'flight_speed': [65.5, 58.2, 72.3],
        'is_venomous': ['no', 'yes', 'no'],
        'breathing_fire_observed': ['no', 'no', 'yes'],
        'observed_by': ['AB', 'TR', 'NR'],
        'year_observed': [2010, 2015, 2020],
        'species': ['Amazonian Blue', 'Peruvian Vipertooth', 'Norwegian Ridgeback']
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_data_with_missing():
    """Create sample data with missing values for testing"""
    data = {
        'gender': ['male', None, 'male'],
        'estimated_age': ['juvenile', 'adult', 'elder'],
        'color_of_scales': ['blue', 'grey', 'green'],
        'color_of_eyes': ['red', 'yellow', 'multicolored'],
        'color_of_wings': ['grey', 'blue', 'purple'],
        'est_body_length': [3.5, 5.2, None],
        'shape_of_snout': ['snub', 'long', 'snub'],
        'shape_of_teeth': ['pointed', 'serrated', 'pointed'],
        'scales_present': ['partial', 'yes', 'no'],
        'scale_texture': ['smooth', 'rough', 'smooth'],
        'body_texture': ['scaled', 'scaled', 'scaled'],
        'snout_length': [0.8, 1.2, 0.9],
        'shape_of_body': ['lithe', 'muscular', 'lithe'],
        'wingspan': [7.2, 10.5, 8.9],
        'number_of_limbs': [2, 4, 2],
        'facial_spikes': ['yes', 'no', 'yes'],
        'frilled': ['yes', 'yes', 'no'],
        'length_of_horns': ['long', 'medium', 'short'],
        'shape_of_horns': ['spiny', 'pointed', 'twisted'],
        'shape_of_tail': ['fluted', 'pointed', 'fluted'],
        'loc_of_sighting': ['Brazil', 'Peru', 'open ocean'],
        'aggressiveness': [4, 6, 3],
        'flight_speed': [65.5, 58.2, 72.3],
        'is_venomous': ['no', 'yes', 'no'],
        'breathing_fire_observed': ['no', 'no', 'yes'],
        'observed_by': ['AB', 'TR', 'NR'],
        'year_observed': [2010, 2015, 2020],
        'species': ['Amazonian Blue', 'Peruvian Vipertooth', 'Norwegian Ridgeback']
    }
    return pd.DataFrame(data)


@pytest.fixture
def encoded_labels():
    """Fixture for label encoding mapping"""
    return {
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


@pytest.fixture
def mock_polynomial_model():
    """Mock polynomial model for testing"""
    model = MagicMock()
    model.predict.return_value = np.array([0, 10, 9])  # Mocked predictions
    return model


@pytest.fixture
def mock_neural_model():
    """Mock neural network model for testing"""
    model = MagicMock()
    model.predict.return_value = np.array([[0.9, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.9, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.9, 0.1, 0, 0]])
    # When using np.argmax on the above, it should return [0, 10, 9]
    return model


# Tests for data processing
def test_preprocess_data(sample_data, encoded_labels):
    """Test data preprocessing function"""
    X, y = preprocess_data(sample_data, encoded_labels)

    # Check that X has the right shape (rows and columns)
    assert X.shape[0] == 3

    # Ensure all categorical features were one-hot encoded
    assert X.shape[1] > 7  # Should have more columns than before

    # Check that labels were encoded correctly
    assert y[0] == 0  # Amazonian Blue
    assert y[1] == 10  # Peruvian Vipertooth
    assert y[2] == 9  # Norwegian Ridgeback


def test_numerical_labels_to_categories():
    """Test conversion from numerical to categorical labels"""
    numerical_labels = np.array([0, 10, 9])
    reverse_mapping = {0: 'Amazonian Blue', 10: 'Peruvian Vipertooth', 9: 'Norwegian Ridgeback'}

    categorical_labels = numerical_labels_to_categories(numerical_labels, reverse_mapping)

    assert categorical_labels[0] == 'Amazonian Blue'
    assert categorical_labels[1] == 'Peruvian Vipertooth'
    assert categorical_labels[2] == 'Norwegian Ridgeback'


# Model specific tests
def test_polynomial_classifier_prediction(mock_polynomial_model, sample_data, encoded_labels):
    """Test polynomial classifier predictions"""
    X, _ = preprocess_data(sample_data, encoded_labels)

    predictions = mock_polynomial_model.predict(X)

    assert len(predictions) == 3
    assert all(isinstance(pred, (int, np.integer)) for pred in predictions)


@patch('tensorflow.keras.dragon_models.Sequential')
def test_neural_network_prediction(mock_sequential, mock_neural_model, sample_data, encoded_labels):
    """Test neural network predictions"""
    X, _ = preprocess_data(sample_data, encoded_labels)

    raw_predictions = mock_neural_model.predict(X)
    predictions = np.argmax(raw_predictions, axis=1)

    assert len(predictions) == 3
    assert all(isinstance(pred, (int, np.integer)) for pred in predictions)
    assert list(predictions) == [0, 10, 9]


# Environment variable tests
def test_model_selection_from_env():
    """Test selecting model based on environment variable"""
    with patch.dict('os.environ', {'MODEL_TYPE': 'polynomial'}):
        model_type = os.environ.get('MODEL_TYPE')
        assert model_type == 'polynomial'

    with patch.dict('os.environ', {'MODEL_TYPE': 'neuralnet'}):
        model_type = os.environ.get('MODEL_TYPE')
        assert model_type == 'neuralnet'


def test_missing_data_handling(sample_data_with_missing, encoded_labels):
    """Test that preprocessing drops rows with missing values"""
    df = pd.DataFrame(sample_data_with_missing)

    test_encoded_labels = {
        'Amazonian Blue': 0,
        'Peruvian Vipertooth': 1,
        'Norwegian Ridgeback': 2
    }

    X, y = preprocess_data(df, test_encoded_labels)

    assert len(X) == 1, "Only one row should remain after dropping rows with NA values"
    assert len(y) == 1, "Only one label should remain after dropping rows with NA values"
    assert y[0] == 0, "The remaining label should be Amazonian Blue (0)"