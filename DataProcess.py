import numpy as np
import pandas as pd

class Data:

    # Constructor
    def __init__(self, type):
        if type == 'train':
            ## Loads in the Data
            data = pd.read_csv(r'/Users/jacksonbrewer/Downloads/loan-train.csv')
            data = pd.DataFrame(data)
        elif type == 'test':
            ## Loads in the Data
            data = pd.read_csv(r'/Users/jacksonbrewer/Downloads/loan-test.csv')
            data = pd.DataFrame(data)

        ## Places the IDs into a separate array and then drops the ID column because it is not a necessary input
        self.applicant_IDs = data['Loan_ID']

        """
        The following code will preprocess all of the data in 
        order for the Network to learn. It will use one-hot 
        encoding for any categorical data and will normalize 
        any numerical column so that it is easier for the network
        to understand. The data will be appended to the inputs 
        array as the program goes
        """

        """ Normalize all the numerical columns """

        ## ApplicantIncome:
        # nan = mean of the column
        x = data['ApplicantIncome']
        mean = np.mean(x)  # Mean of the column
        std = np.std(x)  # Standard Deviation of the column
        data['ApplicantIncome'].fillna(mean, inplace=True)  # Fills blank cells
        x = np.array([data['ApplicantIncome']])  # New array with filled blanks
        norm_x = (x - mean) / std
        data['ApplicantIncome'] = norm_x[0]

        ## CoapplicantIncome:
        # nan = mean of the column
        x = data['CoapplicantIncome']
        mean = np.mean(x)  # Mean of the column
        std = np.std(x)  # Standard Deviation of the column
        data['CoapplicantIncome'].fillna(mean, inplace=True)  # Fills blank cells
        x = np.array([data['CoapplicantIncome']])  # New array with filled blanks
        norm_x = (x - mean) / std
        data['CoapplicantIncome'] = norm_x[0]

        ## LoanAmount:
        # nan = mean of the column
        x = data['LoanAmount']
        mean = np.mean(x)  # Mean of the column
        std = np.std(x)  # Standard Deviation of the column
        data['LoanAmount'].fillna(mean, inplace=True)  # Fills blank cells
        x = np.array([data['LoanAmount']])  # New array with filled blanks
        norm_x = (x - mean) / std
        data['LoanAmount'] = norm_x[0]

        ## Loan_Amount_Term:
        # nan = mean of the column
        x = data['Loan_Amount_Term']
        mean = np.mean(x)  # Mean of the column
        std = np.std(x)  # Standard Deviation of the column
        data['Loan_Amount_Term'].fillna(mean, inplace=True)  # Fills blank cells
        x = np.array([data['Loan_Amount_Term']])  # New array with filled blanks
        norm_x = (x - mean) / std
        data['Loan_Amount_Term'] = norm_x[0]

        ## Credit_History:
        # nan = mean of the column
        x = data['Credit_History']
        mean = np.mean(x)  # Mean of the column
        std = np.std(x)  # Standard Deviation of the column
        data['Credit_History'].fillna(mean, inplace=True)  # Fills blank cells
        x = np.array([data['Credit_History']])  # New array with filled blanks
        norm_x = (x - mean) / std
        data['Credit_History'] = norm_x[0]

        """ Creates and initializes the array that will hold the data as 'inputs' """
        self.inputs = []
        for i, row in data.iterrows():
            inner_inputs = []

            ## Gender:
            # Male = [0,1], Female = [1,0], N/A = [0,0]
            if data.loc[i, 'Gender'] == 'Male':
                inner_inputs.append(0)
                inner_inputs.append(1)
            elif data.loc[i, 'Gender'] == 'Female':
                inner_inputs.append(1)
                inner_inputs.append(0)
            else:
                inner_inputs.append(0)
                inner_inputs.append(0)

            ## Married:
            # Yes = [0,1], No = [1,0], N/A = [0,0]
            if data.loc[i, 'Married'] == 'Yes':
                inner_inputs.append(0)
                inner_inputs.append(1)
            elif data.loc[i, 'Married'] == 'No':
                inner_inputs.append(1)
                inner_inputs.append(0)
            else:
                inner_inputs.append(0)
                inner_inputs.append(0)

            ## Dependents:
            # 0 = [0,0,1], 1 = [0,1,0], 2 = [0,1,1], 3+ = [1,0,0], N/A = [0,0,0]
            if data.loc[i, 'Dependents'] == '0':
                inner_inputs.append(0)
                inner_inputs.append(0)
                inner_inputs.append(1)
            elif data.loc[i, 'Dependents'] == '1':
                inner_inputs.append(0)
                inner_inputs.append(1)
                inner_inputs.append(0)
            elif data.loc[i, 'Dependents'] == '2':
                inner_inputs.append(0)
                inner_inputs.append(1)
                inner_inputs.append(1)
            elif data.loc[i, 'Dependents'] == '3+':
                inner_inputs.append(1)
                inner_inputs.append(0)
                inner_inputs.append(0)
            else:
                inner_inputs.append(0)
                inner_inputs.append(0)
                inner_inputs.append(0)

            ## Education:
            # Graduate = [0,1], Not Graduate = [1,0], N/A = [0,0]
            if data.loc[i, 'Education'] == 'Graduate':
                inner_inputs.append(0)
                inner_inputs.append(1)
            elif data.loc[i, 'Education'] == 'Not Graduate':
                inner_inputs.append(1)
                inner_inputs.append(0)
            else:
                inner_inputs.append(0)
                inner_inputs.append(0)

            ## Self_Employed:
            # Yes = [0,1], No = [1,0], N/A = [0,0]
            if data.loc[i, 'Self_Employed'] == 'Yes':
                inner_inputs.append(0)
                inner_inputs.append(1)
            elif data.loc[i, 'Self_Employed'] == 'No':
                inner_inputs.append(1)
                inner_inputs.append(0)
            else:
                inner_inputs.append(0)
                inner_inputs.append(0)

            ## ApplicantIncome:
            inner_inputs.append(data.loc[i, 'ApplicantIncome'])

            ## CoapplicantIncome:
            inner_inputs.append(data.loc[i, 'CoapplicantIncome'])

            ## LoanAmount:
            inner_inputs.append(data.loc[i, 'LoanAmount'])

            ## Loan_Amount_Term:
            inner_inputs.append(data.loc[i, 'Loan_Amount_Term'])

            ## Credit_History:
            inner_inputs.append(data.loc[i, 'Credit_History'])

            ## Property_Area:
            # Urban = [0,1], Semiurban = [1,0], Rural = [1,1], N/A = [0,0]
            if data.loc[i, 'Property_Area'] == 'Urban':
                inner_inputs.append(0)
                inner_inputs.append(1)
            elif data.loc[i, 'Property_Area'] == 'Semiurban':
                inner_inputs.append(1)
                inner_inputs.append(0)
            elif data.loc[i, 'Property_Area'] == 'Rural':
                inner_inputs.append(1)
                inner_inputs.append(1)
            else:
                inner_inputs.append(0)
                inner_inputs.append(0)

            self.inputs.append(inner_inputs)

        if type == 'train':

            self.target_outputs = []
            ## Loan_Status:
            # Y = [0,1], N = [1,0], N/A = [0,0]
            for i, value in enumerate(data['Loan_Status']):
                if value == 'Y':
                    self.target_outputs.append(1)
                elif value == 'N':
                    self.target_outputs.append(0)
                else:
                    self.target_outputs.append(None)





    # Returns the cleaned data
    def get_inputs(self):
        return self.inputs

    def get_targets(self):
        return self.target_outputs

    def get_applicants(self):
        return self.applicant_IDs

