# IntelligentLoanMachine

The purpose of this project was to implement the Neural Network technology I had coded into something that could be presented as interesting.  

The following link is to a paper showing my derivation and coding of the Neural Network: https://docs.google.com/document/d/15bzee4pXn-5meryFRr5lYqhr-yU2Um5KduAW-x1uhnc/edit?usp=sharing


Neural Networks are able to find complex relationships between input and output data. Knowing this and having the framework of a Neural Network coded, I decided to try and find a data set that included both information about loan applicants and whether or not they were succesful in recieving a loan. 

The data set I used is: https://www.kaggle.com/datasets/vikasukani/loan-eligible-dataset

# Data Processing 
This Kaggle Data Set includes both a training set and a testing set. As seen in the DataProcess.py file I used the Pandas library to download both training and testing sets in order to prepare them to be fed into the Network. 
First I removed the ID column. My next step was to 
