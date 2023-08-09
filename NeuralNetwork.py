import numpy as np

class Network:

    def __init__(self, layer_neurons):
        """
        Constructor for the Network.
        :param layer_neurons: Initializes the number of neurons for each layer of the Network.
        Initializes random weights and biases for each layer in the Network.
        Initializes empty arrays to hold the weighted sums, errors, and activations of the Network.
        """
        self.layer_neurons = layer_neurons # Initializes number of neurons in each layer
        self.nl = len(self.layer_neurons)  # num_layers
        self.w = [np.random.rand(self.layer_neurons[i + 1],self.layer_neurons[i]) for i in range(self.nl - 1)] # Weights
        self.b = [np.random.rand(1,self.layer_neurons[i]) for i in range(1, self.nl)] # Biases
        self.z = [np.zeros((1,self.layer_neurons[i])) for i in range(1,self.nl)] # Weighted Sums
        self.a = [np.zeros((1,self.layer_neurons[i])) for i in range(self.nl)] # Activation Outputs
        self.nabla = [np.zeros((1,self.layer_neurons[i])) for i in range(1, self.nl)] # Errors

    def forward(self, inputs):
        """
        This is the method that propagates through the Network and computes its output.
        :param inputs: Inputs of the Network
        :return: Output of the Network
        Iterates through each layer computing and assigning its weighted sums and its outputs.
        Computes outputs by running it through the sigmoid function.
        :return: the last index in the activation array.
        """
        self.a[0][0] = inputs
        for i in range(self.nl - 2):
            for j in range(self.layer_neurons[i + 1]):
                self.z[i][0][j] = np.dot(self.a[i][0], self.w[i][j]) + self.b[i][0][j]
            self.a[i + 1][0] = self.sigmoid(self.z[i][0])
        for j in range(self.layer_neurons[-1]):
            self.z[-1][0][j] = np.dot(self.a[-2][0], self.w[-1][j]) + self.b[-1][0][j]
        self.a[-1][0] = self.sigmoid(self.z[-1][0])

        return self.a[-1][0]

    def backpropagation(self, x, y):
        """
        Performs the backpropagation of the Network.
        :param x: The inputs
        :param y: The target outputs
        1) Forward propagates through network.
        2) Calculates the error of the output layer and each subsequent one moving backwards.
        3) Computes the partial derivative due to the error and weights
        """

        # Forward
        self.a[0][0] = x
        for i in range(self.nl - 2):
            for j in range(self.layer_neurons[i + 1]):
                self.z[i][0][j] = np.dot(self.a[i][0], self.w[i][j]) + self.b[i][0][j]
            self.a[i + 1][0] = self.sigmoid(self.z[i][0])

        for j in range(self.layer_neurons[-1]):
            self.z[-1][0][j] = np.dot(self.a[-2][0], self.w[-1][j]) + self.b[-1][0][j]
        self.a[-1][0] = self.sigmoid(self.z[-1][0])

        # Backwards
        e = self.a[-1][0] - y
        self.nabla[-1][0] = e * self.sigmoid_deriv(self.z[-1][0])

        for i in range(1, self.nl - 1):
            e = np.dot(self.w[-i].transpose(), self.nabla[-i][0])
            self.nabla[-i - 1][0] = e * self.sigmoid_deriv(self.z[-i - 1][0])

    def update_weights(self, x, y, lr):
        """
        Updates the Weights for the Network
        :param x: Inputs
        :param y: Target Outputs
        :param lr: Learning Rate
        Updates each weight for each layer of the form w = w - α*δ*x
        Updates each bias for each layer of the form b = b - α*δ
        """
        self.backpropagation(x,y)

        for i in range(self.nl - 2):
            for j in range(self.layer_neurons[i + 1]):
                self.w[i][j] -= lr * np.multiply(self.nabla[i][0][j], self.a[i][0])
                self.b[i][0][j] -= lr * self.nabla[i][0][j]
        self.w[-1] -= lr * np.multiply(self.nabla[-1][0][0],self.a[-2][0])
        self.b[-1][0] -= lr * (self.nabla[-1][0][0])

    def train(self, num, xs, ys, lr):
        """
        Training Method
        :param num: Number of training iterations
        :param xs: Array of inputs
        :param ys: Array of Outputs
        :param lr: Learning Rate
        1) Iterates through num
        2) Iterates through each training example
        3) Updates Weights
        """
        for _ in range(num):
            for x, y in zip(xs,ys):
                self.update_weights(x,y,lr)

    def sigmoid(self,z):
        """ Sigmoid Activation Function """
        return 1/(1+np.exp(-z))

    def sigmoid_deriv(self, z):
        """ Derivative of the Sigmoid Function """
        return self.sigmoid(z) * (1 - self.sigmoid(z))
