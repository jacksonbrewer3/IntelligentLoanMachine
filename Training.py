from NeuralNetwork import Network
from DataProcess import Data

"""
This file will take the data from the the loan-train.csv and will train the Network so that 
it is able to take information about a loan applicant and decide whether or not they receive a loan
"""
class Trained_Network:

    def __init__(self):
        ## Utilizes the Data class to initialize the loan-train.csv data
        self.data = Data('train')

        ## Inputs of the Network
        self.X = self.data.get_inputs()

        ## Target outputs of the Network
        self.y = self.data.get_targets()

        ## Declares the number of neurons in each layer of the training network
        layer_neurons = [18, 15, 1]

        ## Initializes the Neural Network
        self.network = Network(layer_neurons)
        lr = 1 # Learning Rate of the Network

        ## Trains the network with the training Data
        self.network.train(10000, self.X, self.y, lr)

    def get_network(self):
        return self.network

