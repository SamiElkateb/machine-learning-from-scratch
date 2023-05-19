import math

class Distance:
    @staticmethod
    def euclidean(q, p):
        if len(q) != len(p): raise Exception("Data should have the same dimension")
        distance = 0
        for i, _ in enumerate(q):
            distance += (q[i]-p[i])**2
        return math.sqrt(distance)

    @staticmethod
    def manhattan(q, p):
        if len(q) != len(p): raise Exception("Data should have the same dimension")
        distance = 0
        for i, _ in enumerate(q):
            distance += abs(q[i]-p[i])
        return distance
