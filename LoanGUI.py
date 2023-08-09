import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import pickle


"""
This file will create the GUI for the Loan Decision Machine. 
The following code will set up the root window.
"""

# Create the root window
root = tk.Tk()
root.title("Loan Calculator")

# Create the frames for the GUI
frame1 = tk.Frame(root)
frame1.pack()
frame2 = tk.Frame(root)
frame2.forget()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 700

# Calculate the x and y position for the window to be centered
x = (screen_width - window_width) // 2
y = ((screen_height - window_height) // 2) - 50

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

"""
The following code will set up what is displayed on the window.
This will allow the user to input their information and the program
will decide to give them a loan or not.
"""

## Data that the network was trained on
training_data = pd.read_csv(r'/Users/jacksonbrewer/Downloads/loan-train.csv')

# Intro Label
intro_text = " Welcome to BrewerBank! If you are here for a loan, please answer the following " \
            "questions to determine your eligibility."
label = tk.Label(frame1, text=intro_text, wraplength=500, anchor='center', font=("Times New Roman", 16))
label.pack(fill='x')

# Filler space below
blank_frame = tk.Frame(frame1, height='30')
blank_frame.pack()

# Loan Questions Header
text = 'Loan Eligibility Questions'
label1 = tk.Label(frame1,text=text,font=("Times New Roman", 14))
label1.pack()

## The Following Code will retrieve and collect the applicants data
inputs = [] # Will hold the answers


"""
Question #1
"""
# Input variable
gender_input_var = tk.StringVar() # Holds the input from the dropdown

# First Question: Gender
text = 'What is your Gender?'
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# First Question Answers:
answers = ["Male","Female"]

# Create the Combobox widget
g_dropdown = ttk.Combobox(frame1, textvariable=gender_input_var, values=answers)
g_dropdown.set("N/A")  # Set the default text for the dropdown
g_dropdown.config(state="readonly")
g_dropdown.pack(anchor=tk.W)



"""
Question #2
"""
# Input variable
marriage_input_var = tk.StringVar() # Holds the input from the dropdown

# 2nd Question: Marital Status
text = 'What is your Marital Status?'
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# 2nd Question Answers:
answers = ["Married","Not Married"]

# Create the Combobox widget
m_dropdown = ttk.Combobox(frame1, textvariable=marriage_input_var, values=answers)
m_dropdown.set("N/A")  # Set the default text for the dropdown
m_dropdown.config(state="readonly")
m_dropdown.pack(anchor=tk.W)

"""
Question #3
"""
# Input variable
dependents_input_var = tk.StringVar() # Holds the input from the dropdown

# 3rd Question: Dependents
text = 'How many dependents do you have?'
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# 3rd Question Answers:
answers = ["0","1","2","3+"]

# Create the Combobox widget
d_dropdown = ttk.Combobox(frame1, textvariable=dependents_input_var, values=answers)
d_dropdown.set("N/A")  # Set the default text for the dropdown
d_dropdown.config(state="readonly")
d_dropdown.pack(anchor=tk.W)

"""
Question #4
"""
# Input variable
education_input_var = tk.StringVar() # Holds the input from the dropdown

# 4th Question: Education
text = 'Did you graduate high school?'
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# 4th Question Answers:
answers = ["Yes","No"]

# Create the Combobox widget
e_dropdown = ttk.Combobox(frame1, textvariable=education_input_var, values=answers)
e_dropdown.set("N/A")  # Set the default text for the dropdown
e_dropdown.config(state="readonly")
e_dropdown.pack(anchor=tk.W)

"""
Question #5
"""
# Input variable
self_employment_input_var = tk.StringVar() # Holds the input from the dropdown

# 5th Question: Self Employment
text = 'Are you Self Employed?'
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# 5th Question Answers:
answers = ["Yes","No"]

# Create the Combobox widget
se_dropdown = ttk.Combobox(frame1, textvariable=self_employment_input_var, values=answers)
se_dropdown.set("N/A")  # Set the default text for the dropdown
se_dropdown.config(state="readonly")
se_dropdown.pack(anchor=tk.W)

"""
Question #6
"""
# Input variable
applicant_income_input_var = tk.StringVar() # Holds the input from the dropdown

# 6th Question: Applicant Income
text = 'What is your monthly income?'
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# Entry widget for user input
ai_entry = tk.Entry(frame1, textvariable=applicant_income_input_var, width=30)
ai_entry.pack(anchor=tk.W)


"""
Question #7
"""
# Input variable
coapplicant_income_input_var = tk.StringVar() # Holds the input from the dropdown

# 7th Question: Co-applicant Income
text = "What is your co-applicant's monthly income? (If you don't have one put 0)"
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# Entry widget for user input
cai_entry = tk.Entry(frame1, textvariable=coapplicant_income_input_var, width=30)
cai_entry.pack(anchor=tk.W)

"""
Question #8
"""
# Input variable
loan_amount_input_var = tk.StringVar() # Holds the input from the dropdown

# 8th Question: Loan Amount
text = "What is the loan you want to receive?"
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# Entry widget for user input
la_entry = tk.Entry(frame1, textvariable=loan_amount_input_var, width=30)
la_entry.pack(anchor=tk.W)

"""
Question #9
"""
# Input variable
loan_term_input_var = tk.StringVar() # Holds the input from the dropdown

# 8th Question: Loan Amount
text = "How long do you want this loan to be for in months? "
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# Entry widget for user input
lt_entry = tk.Entry(frame1, textvariable=loan_term_input_var, width=30)
lt_entry.pack(anchor=tk.W)

"""
Question #10
"""
# Input variable
credit_score_input_var = tk.StringVar() # Holds the input from the dropdown

# 11th Question: Credit Score
text = "If your FICO score is above 700, select 1. Otherwise select 0."
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# 10th Question Answers:
answers = ["0","1"]

# Create the Combobox widget
cs_dropdown = ttk.Combobox(frame1, textvariable=credit_score_input_var, values=answers)
cs_dropdown.set("N/A")  # Set the default text for the dropdown
cs_dropdown.config(state="readonly")
cs_dropdown.pack(anchor=tk.W)

"""
Question #11
"""
# Input variable
property_area_input_var = tk.StringVar() # Holds the input from the dropdown

# 11th Question: Living Area
text = "Which area do you live in?"
label = tk.Label(frame1,text=text, font=("Times New Roman", 14))
label.pack(side=tk.TOP, anchor=tk.W)

# 11th Question Answers:
answers = ["Urban","Semiurban", "Rural"]

# Create the Combobox widget
pa_dropdown = ttk.Combobox(frame1, textvariable=property_area_input_var, values=answers)
pa_dropdown.set("N/A")  # Set the default text for the dropdown
pa_dropdown.config(state="readonly")
pa_dropdown.pack(anchor=tk.W)

"""
The following code will take the answers of the user as input
and feed it through the existing loan model in order to predict
whether or not the applicant receives a loan. 
"""

## Loads in the Neural Network for the loan decision
with open('saved_model.pkl', 'rb') as file:
    trained_model = pickle.load(file)

def on_button_click():

    """
    Fill the inputs list with the inputs of the user
    """

    ## Gender Input
    g_input = gender_input_var.get()
    if g_input == 'Male':
        inputs.append(0)
        inputs.append(1)
    elif g_input == 'Female':
        inputs.append(1)
        inputs.append(0)
    else:
        inputs.append(0)
        inputs.append(0)

    ## Married Input
    m_input = marriage_input_var.get()
    if m_input == 'Married':
        inputs.append(0)
        inputs.append(1)
    elif m_input == 'Not Married':
        inputs.append(1)
        inputs.append(0)
    else:
        inputs.append(0)
        inputs.append(0)

    ## Dependents Inputs
    d_input = dependents_input_var.get()
    if d_input == '0':
        inputs.append(0)
        inputs.append(0)
        inputs.append(1)
    elif d_input == '1':
        inputs.append(0)
        inputs.append(1)
        inputs.append(0)
    elif d_input == '2':
        inputs.append(0)
        inputs.append(1)
        inputs.append(1)
    elif d_input == '3+':
        inputs.append(1)
        inputs.append(0)
        inputs.append(0)
    else:
        inputs.append(0)
        inputs.append(0)
        inputs.append(0)

    ## Education Inputs
    e_input = education_input_var.get()
    if e_input == 'Yes':
        inputs.append(0)
        inputs.append(1)
    elif e_input == 'No':
        inputs.append(1)
        inputs.append(0)
    else:
        inputs.append(0)
        inputs.append(0)

    ## Self Employed Inputs
    se_input = self_employment_input_var.get()
    if se_input == 'Yes':
        inputs.append(0)
        inputs.append(1)
    elif se_input == 'No':
        inputs.append(1)
        inputs.append(0)
    else:
        inputs.append(0)
        inputs.append(0)

    ## Applicant Income Input
    ai_input = applicant_income_input_var.get()
    ai_input = int(ai_input)
    # Normalizes input
    x = training_data['ApplicantIncome']
    mean = np.mean(x)
    std = np.std(x)
    norm_ai_input = (ai_input - mean)/std
    inputs.append(norm_ai_input)

    ## Copplicant Income Input
    cai_input = coapplicant_income_input_var.get()
    cai_input = int(cai_input)
    # Normalizes input
    x = training_data['CoapplicantIncome']
    mean = np.mean(x)
    std = np.std(x)
    norm_cai_input = (cai_input - mean) / std
    inputs.append(norm_cai_input)

    ## Loan Amount Input
    la_input = loan_amount_input_var.get()
    la_input = int(la_input)
    # Normalizes input
    x = training_data['LoanAmount']
    mean = np.mean(x)
    std = np.std(x)
    norm_la_input = (la_input - mean) / std
    inputs.append(norm_la_input)

    ## Loan Term Input
    lt_input = loan_term_input_var.get()
    lt_input = int(lt_input)
    # Normalizes input
    x = training_data['Loan_Amount_Term']
    mean = np.mean(x)
    std = np.std(x)
    norm_lt_input = (lt_input - mean) / std
    inputs.append(norm_lt_input)

    ## Credit History Input
    ch_input = credit_score_input_var.get()
    ch_input = int(ch_input)
    # Normalizes input
    x = training_data['Credit_History']
    mean = np.mean(x)
    std = np.std(x)
    norm_ch_input = (ch_input - mean) / std
    inputs.append(norm_ch_input)

    ## Property Area Inputs
    pa_input = property_area_input_var.get()
    if pa_input == 'Urban':
        inputs.append(0)
        inputs.append(1)
    elif pa_input == 'Semiurban':
        inputs.append(1)
        inputs.append(0)
    elif pa_input == 'Rural':
        inputs.append(1)
        inputs.append(1)
    else:
        inputs.append(0)
        inputs.append(0)

    output = trained_model.forward(inputs)

    frame1.forget()
    frame2.pack()

    blank_frame = tk.Frame(frame2, height='300')
    blank_frame.pack()

    if output > .5:
        text = f"Congratulations! You are eligible for a loan from BrewerBank. Your impressive model " \
               f"score of {output} was enough to be approved."
        label = tk.Label(frame2, text=text, wraplength=500, anchor='center', font=("Times New Roman", 16))
        label.pack(anchor='center')
    else:
        text = f"We are sorry to inform you that you are intelligible at this time to receive a loan." \
               f"Unfortunately your model score of {output} was not enough to be approved."
        label = tk.Label(frame2, text=text, wraplength=500, anchor='center', font=("Times New Roman", 16))
        label.pack(expand=True, fill='both')

button = tk.Button(frame1, text="Submit Information", command=on_button_click)
button.pack()









# Start the GUI event loop
root.mainloop()

print(inputs)