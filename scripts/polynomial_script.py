"""Script for building Polynomial classification model"""
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from models.polynomial_model import PolynomialClassifier
from utils.helper import create_main_dataframe, preprocess_data, numerical_labels_to_categories

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
    :param: none
    :return: none
    """
    # concatenate data into single dataframe
    main_df = create_main_dataframe()
    print(main_df.head(3))

    # get features and labels
    X, y = preprocess_data(main_df, encoded_labels)

    # split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model2 = PolynomialClassifier(degree=1)
    model2.fit(X_train, y_train)

    model2_preds = model2.predict(X_test)

    model2_preds_converted = numerical_labels_to_categories(model2_preds, reverse_labels)
    y_test_converted = numerical_labels_to_categories(y_test, reverse_labels)

    accuracy2 = accuracy_score(y_test_converted, model2_preds_converted)
    print("Accuracy 2:", accuracy2)


if __name__ == '__main__':
    main()
