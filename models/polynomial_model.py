""" polynomial model class to use for classification"""
import numpy as np


class PolynomialClassifier:
    def __init__(self, degree):
        self.degree = degree
        self.coefficients = None

    def fit(self, X, y):
        X_poly = self._polynomial_features(X)
        self.coefficients = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ y

    def predict(self, X):
        X_poly = self._polynomial_features(X)
        y_pred = X_poly @ self.coefficients
        return np.round(y_pred)

    def _polynomial_features(self, X):
        X_poly = np.ones((len(X), 1))
        for d in range(1, self.degree + 1):
            X_poly = np.hstack((X_poly, X ** d))
        return X_poly

# Example usage
X_train = np.array([[1], [2], [3], [4], [5], [6]])
y_train = np.array([0, 0, 1, 1, 2, 2])

model = PolynomialClassifier(degree=2)
model.fit(X_train, y_train)

X_test = np.array([[2.5], [4.5]])
y_pred = model.predict(X_test)

print("Predicted classes:", y_pred)

'''In this script, the PolynomialClassifier class is defined with an __init__ method, a fit method, and a predict method. 
The fit method takes the training data X and y and fits the polynomial coefficients using the normal equation. 
The predict method takes new data X and predicts the class labels based on the learned coefficients. The 
_polynomial_features method is a helper function that transforms the input features into polynomial features.

In the example usage, we create a PolynomialClassifier object with a degree of 2, fit it on the training data, 
and then use it to predict the classes for new data points. The predicted classes are printed as output.

Certainly! Let's break down the function step by step:

X_poly.T: This takes the transpose of the polynomial features matrix X_poly. The transpose operation flips the rows and 
columns of the matrix.

X_poly.T @ X_poly: This performs matrix multiplication between the transpose of X_poly and X_poly itself. This 
operation calculates the dot product of the transposed matrix with itself.

np.linalg.inv(X_poly.T @ X_poly): This uses the inv() function from the NumPy linalg module to calculate the inverse 
of the matrix obtained from the previous step. The inverse of a matrix is a matrix that, when multiplied with the 
original matrix, gives the identity matrix.

X_poly.T @ y: This performs matrix multiplication between the transpose of X_poly and the target variable y. 
This operation calculates the dot product of the transposed matrix with the target variable.

np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ y: This combines the previous steps to calculate the coefficients of 
the polynomial equation. It multiplies the inverse of the matrix X_poly.T @ X_poly with the matrix X_poly.T @ y.

In summary, this function calculates the coefficients of the polynomial equation by performing matrix operations. It 
uses the transpose, matrix multiplication, and matrix inverse operations to find the best-fitting curve through the 
data points.'''

'''Imagine you have a bunch of data points that represent different creatures. Each creature has some features, 
like size or weight, and we want to predict what species of dragon each creature is. But here's the catch: the 
relationship between the features and the species might not be a simple straight line. It could be more complex, 
like a curve or a wavy line.

That's where polynomial classification comes in! We use polynomials to capture these more complex relationships. 
A polynomial is just a fancy math term for an equation with different powers of a variable. In our case, the variable 
represents the features of the creatures.

Let's say we have one feature, like the size of the creature. We can start with a simple linear equation: y = mx + b. 
In this equation, y represents the species of the creature, x represents the size, m represents the slope, and b 
represents the y-intercept. But if the relationship between size and species is more complex, a straight line won't 
cut it.

So, we can make the equation more flexible by adding higher powers of x. For example, we can have a quadratic equation: 
y = ax^2 + bx + c. Now, we have three coefficients: a, b, and c. These coefficients determine the shape of the curve. 
By adjusting these coefficients, we can fit the curve to our data points.

But how do we find the best values for these coefficients? That's where the "fit" method comes in. It uses a technique 
called the normal equation to find the optimal coefficients that minimize the difference between the predicted species 
and the actual species in the training data. It's like finding the best-fitting curve through the data points.

Once we have the coefficients, we can use the "predict" method to make predictions for new creatures. We plug in the 
features of a new creature into our polynomial equation, and it gives us a predicted species. We can round the result 
to the nearest whole number to get a discrete species label.

And that's polynomial classification in a nutshell, Bill Nye style! It's a way to capture more complex relationships 
between features and species using polynomial equations. By adjusting the coefficients, we can fit curves to our data 
and make predictions for new creatures.'''