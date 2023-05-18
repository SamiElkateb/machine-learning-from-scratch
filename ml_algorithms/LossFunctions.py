class LossFunctions:
    @staticmethod
    def mse(y, y_pred):
        n = len(y)
        tmp = 0
        for i in range(n):
            tmp += 1/n*(y[i]-y_pred[i])**2
        return tmp
