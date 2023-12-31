import numpy as np
from diabete_prediction_model.utils.simple_linear_regr_utils import generate_data, evaluate


class SimpleLinearRegression:
    def __init__(self, iterations=15000, lr=0.1):
        self.iterations = iterations # number of iterations the fit method will be called
        self.lr = lr # The learning rate
        self.losses = [] # A list to hold the history of the calculated losses
        self.W, self.b = None, None # the slope and the intercept of the model

    def __loss(self, y, y_hat):
        """

        :param y: the actual output on the training set
        :param y_hat: the predicted output on the training set
        :return:
            loss: the sum of squared error

        """
        loss = np.sum((y - y_hat) ** 2)

        self.losses.append(loss)
        return loss

    def __init_weights(self, X):
        """

        :param X: The training set
        """
        weights = np.random.normal(size=X.shape[1] + 1)
        self.W = weights[:X.shape[1]].reshape(-1, X.shape[1])
        self.b = weights[-1]
        
    def __gradient(self, X, y):
        """
        :param X: The training sample
        :param y: The actual output of the training sample
        
        :return:
            dW: the derivative of slope 
            db: the derivative of intercept
        """
        y_pred = self.predict(X)
        error = y_pred - y
        dW = 2 * np.dot(X.T, error) / y.shape[0]
        db = 2 * np.mean(error)
        return dW, db
    
    def __sgd(self, X, y, y_hat):
        """

        :param X: The training set
        :param y: The actual output on the training set
        :param y_hat: The predicted output on the training set
        :return:
            sets updated W and b to the instance Object (self)
        """
        n_obs = X.shape[0]

        # Shuffle the data
        indices = np.random.permutation(n_obs)
        X = X[indices]
        y = y[indices]
        
        X_i = X[0]
        y_i = y[0]
        
        # calcuate the gradient
        gradient = self.__gradient(X_i, y_i)
        dW = gradient[0]
        db = gradient[1]
        
        # update W and b with derivate and learning rate
        self.W -= self.lr * dW
        self.b -= self.lr * db


    def fit(self, X, y):
        """

        :param X: The training set
        :param y: The true output of the training set
        :return:
        """
        self.__init_weights(X)
        y_hat = self.predict(X)
        loss = self.__loss(y, y_hat)
        print(f"Initial Loss: {loss}")
        for i in range(self.iterations + 1):
            self.__sgd(X, y, y_hat)
            y_hat = self.predict(X)
            loss = self.__loss(y, y_hat)
            if not i % 100:
                print(f"Iteration {i}, Loss: {loss}")

    def predict(self, X):
        """

        :param X: The training dataset
        :return:
            y_hat: the predicted output
        """
        y_hat = np.dot(X, self.W) + self.b
        return y_hat


if __name__ == "__main__":
    X_train, y_train, X_test, y_test = generate_data()
    model = SimpleLinearRegression()
    model.fit(X_train,y_train)
    predicted = model.predict(X_test)
    evaluate(model, X_test, y_test, predicted)