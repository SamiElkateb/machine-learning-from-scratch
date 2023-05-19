class Vector:
    def __init__(self, data: list[float]):
        self.data = data

    def print(self):
        data = self.data
        print("[", end="")
        for i, x in enumerate(data):
            if i == len(data) - 1:
                print(x, end="")
            else:
                print(x, end=", ")
        print("]")

    def add(self, value):
        return self.__arithmetics(value, "addition")

    def multiply(self, value):
        return self.__arithmetics(value, "multiplication")

    def substract(self, value):
        return self.__arithmetics(value, "substraction")

    @staticmethod
    def substraction(v1, v2):
        data_v1 = v1.data
        data_v2 = v2.data
        tmp = []
        for x, _ in enumerate(data_v1):
            tmp[x].append(data_v1[x] - data_v2[x])
        return Vector(tmp)

    @staticmethod
    def zeros(number):
        tmp = [0.0 for _ in range(number)]
        return Vector(tmp)

    @staticmethod
    def sum(vector):
        tmp = 0
        for _, x in enumerate(vector.data):
            tmp += x
        return tmp

    def clone(self):
        tmp = [i for _, i in enumerate(self.data)]
        return Vector(tmp)

    def __arithmetics(self, value, sign):
        vector = self.clone()
        if isinstance(value, (int, float)):
            for x, _ in enumerate(vector.data):
                if sign == 'addition':
                    vector.data[x] += value
                elif sign == 'substraction':
                    vector.data[x] -= value
                elif sign == 'multiplication':
                    vector.data[x] *= value
                elif sign == 'division':
                    vector.data[x] /= value
                else:
                    raise Exception("Arithmetic sign not valid")
        elif isinstance(value, Vector):
            vector_data = value.data
            for x, _ in enumerate(vector.data):
                if sign == 'addition':
                    vector.data[x] += vector_data[x]
                elif sign == 'substraction':
                    vector.data[x] -= vector_data[x]
                elif sign == 'multiplication':
                    vector.data[x] *= vector_data[x]
                elif sign == 'division':
                    vector.data[x] /= vector_data[x]
                else:
                    raise Exception("Arithmetic sign not valid")
        else:
            raise Exception(
                "Arithmetics of Vector should be of type Vector or Scalar")
        return vector
