from .Vector import Vector
class Matrix:
    def __init__(self, data:list[list[float]]):
        self.data = data

    def transpose(self):
        data = self.data
        tmp = [[] for _ in range(len(data[0]))]
        for i, _ in enumerate(data):
            for j, _ in enumerate(data[i]):
                tmp[j].append(data[i][j])
        return Matrix(tmp)

    def shape(self):
        nb_samples = len(self.data)
        nb_features = len(self.data[0])
        return nb_samples, nb_features

    def add(self, value):
        return self.__arithmetics(value, "addition")

    def multiply(self, value):
        return self.__arithmetics(value, "multiplication")

    def substract(self, value):
        return self.__arithmetics(value, "substraction")

    def map(self, fn):
        tmp = []
        for _, x in enumerate(self.data):
            tmp.append(fn(x))
        return tmp


    @staticmethod
    def dot(m1, m2):
        data_m1 = m1.data
        data_m2 = m2.data
        if isinstance(m2, Matrix):
            tmp = [[] for _ in enumerate(data_m1)]
            for i, _ in enumerate(data_m1):
                for j, _ in enumerate(data_m2[0]):
                    res = 0
                    for k, _ in enumerate(data_m1[0]):
                        res += data_m1[i][k] * data_m2[k][j]
                    tmp[i].append(res)
            return Matrix(tmp)
        elif isinstance(m2, Vector):
            tmp = []
            for i, _ in enumerate(data_m1):
                res = 0
                for k, _ in enumerate(data_m1[0]):
                    res += data_m1[i][k] * data_m2[k]
                tmp.append(res)
            return Vector(tmp)
        else: raise Exception("Dot product should be between two matrices or a matrix and a vector")

    @staticmethod
    def sum(matrix):
        tmp = 0
        for _, x in enumerate(matrix.data):
            for _, y in enumerate(x):
                tmp += y
        return tmp

    def print(self):
        data = self.data
        print("[", end="")
        for i, x in enumerate(data):
            print("[", end="")
            for j, y in enumerate(x):
                if j == len(x) - 1:
                    print(y, end="")
                else:
                    print(y, end=", ")
            if i == len(data) - 1:
                print("]", end="")
            else:
                print("]")
        print("]")

    def clone(self):
        tmp = [y for _, y in enumerate(x for _, x  in enumerate(self.data))]
        return Matrix(tmp)

    def __arithmetics(self, value, sign):
        matrix = self.clone()
        if isinstance(value, (int, float)):
            for x, _ in enumerate(matrix.data):
                for y, _ in enumerate(matrix.data[x]):
                    if sign == 'addition':
                        matrix.data[x][y] += value
                    elif sign == 'substraction':
                        matrix.data[x][y] -= value
                    elif sign == 'multiplication':
                        matrix.data[x][y] *= value
                    elif sign == 'division':
                        matrix.data[x][y] /= value
                    else:
                        raise Exception("Arithmetic sign not valid")
        elif isinstance(value, Vector):
            vector_data = value.data
            for x, _ in enumerate(matrix.data):
                for y, _ in enumerate(matrix.data[x]):
                    if sign == 'addition':
                        matrix.data[x][y] += vector_data[x]
                    elif sign == 'substraction':
                        matrix.data[x][y] -= vector_data[x]
                    elif sign == 'multiplication':
                        matrix.data[x][y] *= vector_data[x]
                    elif sign == 'division':
                        matrix.data[x][y] /= vector_data[x]
                    else:
                        raise Exception("Arithmetic sign not valid")
        elif isinstance(value, Matrix):
            matrix_data = value.data
            for x, _ in enumerate(matrix.data):
                for y, _ in enumerate(matrix.data[x]):
                    if sign == 'addition':
                        matrix.data[x][y] += matrix_data[x][y]
                    elif sign == 'substraction':
                        matrix.data[x][y] -= matrix_data[x][y]
                    elif sign == 'multiplication':
                        matrix.data[x][y] *= matrix_data[x][y]
                    elif sign == 'division':
                        matrix.data[x][y] /= matrix_data[x][y]
                    else:
                        raise Exception("Arithmetic sign not valid")
        else: raise Exception("Arithmetics of Matrix should be of type Matrix, Vector or Scalar")
        return matrix

