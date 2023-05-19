from .Matrix import Matrix, Vector
from .utils import Distance

class KNN:
    def __init__(self, k=5, distance="euclidean"):
        self.k = k
        self.distance_algorithm = getattr(Distance, distance)

    def fit(self, X: Matrix, y: Vector):
        self.X_train = X
        self.y_train = y

    def predict(self, X: Matrix):
        y_pred = []
        for _, x in enumerate(X.data):
            y_pred.append(self._predict(x))
        return Vector(y_pred)

    def _predict(self, x):
        distances = []
        for _, x_train in enumerate(self.X_train.data):
            distance = self.distance_algorithm(x_train, x)
            distances.append(distance)

        # can be done in the same loop as the distance calculation, 
        # separated for clarity
        sorted_values = []
        k_nearest_labels = []
        for i, x in enumerate(distances):
            j = 0
            while j < len(sorted_values) and x > sorted_values[j]:
                j += 1
            sorted_values.insert(j, x)
            k_nearest_labels.insert(j, self.y_train.data[i])
        k_nearest_labels = k_nearest_labels[:self.k]

        counts = {}
        for item in k_nearest_labels:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[0][0]
