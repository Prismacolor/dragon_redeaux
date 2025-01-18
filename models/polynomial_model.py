"""
    polynomial model class to use for classification
    utilizes ridge regression(calculated as sum of squared magnitudes of coefficients x alpha
    higher alpha means more regularization/higher penalties, this is to prevent overfitting

"""
import numpy as np


class PolynomialClassifier:
    def __init__(self, degree, alpha=0.5):
        self.degree = degree
        self.coefficients = None
        self.alpha = alpha  # for regularization

    def fit(self, X, y):
        X_poly = self._polynomial_features(X)
        identity = np.eye(X_poly.shape[1])
        self.coefficients = np.linalg.inv(X_poly.T @ X_poly + self.alpha * identity) @ X_poly.T @ y  # use ridge regression to avoid singular matrix

    def predict(self, X):
        X_poly = self._polynomial_features(X)
        y_pred = X_poly @ self.coefficients

        return np.round(y_pred)

    def _polynomial_features(self, X):
        X_poly = np.ones((len(X), 1))
        for d in range(1, self.degree + 1):
            X_poly = np.hstack((X_poly, X ** d))
        return X_poly


