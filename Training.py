from NeuralNetwork import Network
from DataProcess import Data

"""
This Project is designed to emulate an intelligent loan decision system. 
I will import anonymous credit data from a bank with identifying information and whether or not they would receive a loan.
I will then use a Neural Network to be the framework for the system and train it with this data.
The Network will then be able to take information about a loan applicant and decide if they get a loan or not
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

