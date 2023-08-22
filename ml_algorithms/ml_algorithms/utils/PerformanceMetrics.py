from ..Vector import Vector


class PerformanceMetrics:
    @staticmethod
    def accuracy(v1: Vector, v2: Vector):
        nb_true = 0
        nb_values = len(v1.data)
        if len(v1.data) != len(v2.data):
            raise Exception("Data should have the same dimension")
        for i in range(len(v1.data)):
            if v1.data[i] == v2.data[i]:
                nb_true += 1
        return nb_true / nb_values
