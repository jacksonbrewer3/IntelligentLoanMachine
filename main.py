import pickle
from DataProcess import Data
import random

with open('saved_model.pkl', 'rb') as file:
    trained_model = pickle.load(file)

data = Data('train')
data_inputs = data.get_inputs()
data_app_ids = data.get_applicants()


for i, applicant in enumerate(data_app_ids):
    output = trained_model.forward(data_inputs[i])
    print(f'Input: {applicant}, Output: {output}')

