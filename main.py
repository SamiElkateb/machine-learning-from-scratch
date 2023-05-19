from sklearn.model_selection import train_test_split
from sklearn import datasets
from ml_algorithms import LinearRegression, LossFunctions, Matrix, Vector, KNN, PerformanceMetrics

def KNNExample():
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    knn = KNN()
    X_train = Matrix(X_train.tolist())
    y_train = Vector(y_train.tolist())
    y_test = Vector(y_test.tolist())
    X_test = Matrix(X_test.tolist())
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = PerformanceMetrics.accuracy(y_pred, y_test)
    print("Accuracy:", acc)

KNNExample()

def LinearRegressionExample():
    X, y = datasets.make_regression(
        n_samples=400, n_features=1, noise=20, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    linear_regression = LinearRegression(learning_rate=0.001)

    X_train = Matrix(X_train.tolist())
    y_train = Vector(y_train.tolist())

    linear_regression.fit(X_train, y_train)

    X_test = Matrix(X_test.tolist())
    predictions = linear_regression.predict(X_test)
    mse_res = LossFunctions.mse(y_test, predictions.data)
    print("MSE: ", mse_res)

