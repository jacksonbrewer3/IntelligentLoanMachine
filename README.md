# IntelligentLoanMachine

The purpose of this project was to implement the Neural Network technology I had coded into something that could be presented as interesting.  

The following link is to a paper showing my derivation and coding of the Neural Network: https://docs.google.com/document/d/15bzee4pXn-5meryFRr5lYqhr-yU2Um5KduAW-x1uhnc/edit?usp=sharing


Neural Networks are able to find complex relationships between input and output data. Knowing this and having the framework of a Neural Network coded, I decided to try and find a data set that included both information about loan applicants and whether or not they were succesful in recieving a loan. 

The data set I used is: https://www.kaggle.com/datasets/vikasukani/loan-eligible-dataset

# Data Processing 
This Kaggle Data Set includes both a training set and a testing set. As seen in the DataProcess.py file I used the Pandas library to download both training and testing sets in order to prepare them to be fed into the Network. 

First I removed the ID column. 

My next step was to prepare all of the columns that held numerical data. I first filled in all of the empty cells with the mean of that column. Next I normalized each column in relation to their means and standard deviations to give the machine a normal distribution to make decisions from. 

My final step was to prepare the columns that held catagorical data. I first filled all of the empty slots with 'N/A'. The next step was to convert the Data in each catagory into numbers that could be fed into the Network. In order to prevent the machine from devloping some ordinal relationship between answers in a column, I used [0,0], [0,1], [1,0] , etc instead of 0, 1, 2, etc. 

Now all the data was cleaned and ready to be fed through the Network in order to train it. 

# Training the Network
After training the data, it was time to train the Neural Network. The Training.py file creates a new Neural Network and feeds the newly cleaned training data through it. I then used Python's pickle process, as seen in PickledNetwork.py, in order to save an instance of the trained Network so that it did not have to be trainied every time the final code was run. 

As seen in the Training.py file, the Network is created with 18 input neurons, 1 output neuron and 1 hidden layer of 15 neurons. Due to the nature of the problem the number of input and output neurons was not subject to change. But changing the number of hidden layers and neurons in each layer of a Neural Network will change its effectivness. After testing different Network structures, the version that proved to be most effective was one with only 1 hidden layer holding 15 neurons. Any more layers or neurons and the program would have run unecessarily long. Any fewer and it would be less accurate. 

In order to test its effectivness I fed each applicant through the trained network and compared the Networks answer to what it is supposed to be. A number close to 1 means they would receive a loan and a number close to 0 means the would not. 

Here is a link to the outputs of the Network: https://docs.google.com/document/d/13br9rXtId7BwNRDQL9J0BWboZSKL25iR3iwKAsWEI14/edit?usp=sharing



