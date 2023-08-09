from Training import Trained_Network
from DataProcess import Data
import pickle

model = Trained_Network()
trained_model = model.get_network()

## Pickles the trained network
with open('saved_model.pkl', 'wb') as file:
    pickle.dump(trained_model, file)


