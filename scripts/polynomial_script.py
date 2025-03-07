"""Script for building Polynomial classification model"""
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import pickle

from models.polynomial_model import PolynomialClassifier
from utils.helper import create_main_dataframe, preprocess_data, numerical_labels_to_categories

models_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models")

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
    main function for processing data and building/training model
    :params: none
    :return: none
    """
    # concatenate data into single dataframe
    main_df = create_main_dataframe()
    print(main_df.head(9))

    # get features and labels
    X, y = preprocess_data(main_df, encoded_labels)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    poly_model = PolynomialClassifier(degree=3)
    poly_model.fit(X_train, y_train)

    polymodel_preds = poly_model.predict(X_test)

    polymodel_preds_converted = numerical_labels_to_categories(polymodel_preds, reverse_labels)
    y_test_converted = numerical_labels_to_categories(y_test, reverse_labels)

    accuracy = accuracy_score(y_test_converted, polymodel_preds_converted)
    print("Accuracy:", accuracy)

    if accuracy > 0.75:
        with open('polynomial_model.pkl', 'wb') as file:
            model_path = os.path.join(models_dir, "dragon_poly_model.pkl")
            pickle.dump(poly_model, file)


if __name__ == '__main__':
    main()
