from .Matrix import Matrix
from .Vector import Vector


class LinearRegression:
    def __init__(self, learning_rate=0.001, n_iterations=10000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X: Matrix, y: Vector):
        n_samples, n_features = X.shape()
        self.weights = Vector.zeros(n_features)
        self.bias = 0
        for _ in range(self.n_iterations):
            y_pred = (X @ self.weights) + self.bias
            dw = (X.transpose() @ (y_pred - y)) * (1 / n_samples)
            db = (1 / n_samples) * Vector.sum(y_pred - y)
            self.weights = self.weights - (dw * self.learning_rate)
            self.bias = self.bias - self.learning_rate * db

    def predict(self, X):
        if self.weights is None:
            raise Exception("Train model before predicting")
        return (X @ self.weights) + self.bias
