from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Project directory: {project_dir}")
sys.path.insert(0, project_dir)

from utils.helper import create_main_dataframe, preprocess_data, numerical_labels_to_categories
from api_model_classes.neuralnetmodel import NeuralNetworkClassifier

models_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dragon_models")

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


def main():
    """
    Main function for processing data and building neural network model
    :params: none
    :returns: none
    """
    main_df = create_main_dataframe()
    print(main_df.head(9))

    X, y = preprocess_data(main_df, encoded_labels)

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    print(f"Data split: Train: {X_train.shape[0]}, Validation: {X_val.shape[0]}, Test: {X_test.shape[0]}")

    nn_model = NeuralNetworkClassifier()
    nn_model.build_model(input_shape=X_train.shape[1])

    nn_model.fit(X_train, y_train, X_val, y_val, epochs=100, batch_size=64)

    loss, accuracy = nn_model.evaluate(X_test, y_test)
    print(f"test set loss: {loss:.2f}")
    print(f"test set accuracy: {accuracy:.2f}")

    nn_preds = nn_model.predict(X_test)
    nn_preds_converted = numerical_labels_to_categories(nn_preds, reverse_labels)
    y_test_converted = numerical_labels_to_categories(y_test, reverse_labels)

    accuracy = accuracy_score(y_test_converted, nn_preds_converted)
    print(f"converted test set accuracy: {accuracy:.2f}")

    if accuracy > 0.75:
        model_path = os.path.join(models_dir, "neuralnet_model.joblib")
        # with open(model_path, 'wb') as file:
        #     pickle.dump(nn_model, file)
        joblib.dump(nn_model, model_path)
        print(f"Model saved to {model_path}")
    else:
        print("Model accuracy is below threshold.")


if __name__ == "__main__":
    main()