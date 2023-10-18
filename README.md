# IntelligentLoanMachine

This project utilized the ability of Neural Networks to find complex relationships between input and output data in order to create a system that could make intelligent decisions on whether or not an applicant should receive a loan.   

The following link is to a paper showing my derivation and coding of the Neural Network: https://docs.google.com/document/d/15bzee4pXn-5meryFRr5lYqhr-yU2Um5KduAW-x1uhnc/edit?usp=sharing


Neural Networks are able to find complex relationships between input and output data. Knowing this and having the framework of a Neural Network coded, I decided to find a data set that included both information about loan applicants and whether or not they were successful in recieving a loan. 

The data set I used is: https://www.kaggle.com/datasets/vikasukani/loan-eligible-dataset

## Data Processing 
This Kaggle Data Set includes both a training set and a testing set. As seen in the DataProcess.py file I used the Pandas library to download both training and testing sets in order to prepare them to be fed into the Network. 

1) First I removed the ID column. 

2) My next step was to prepare all of the columns that held numerical data. I first filled in all of the empty cells with the mean of that column. Next I normalized each column in relation to their means and standard deviations to give the machine a normal distribution to make decisions from. 

3) My final step was to prepare the columns that held categorical data. I first filled all of the empty slots with 'N/A'. The next step was to convert the Data in each category into numbers that could be fed into the Network. In order to prevent the machine from developing some ordinal relationship between answers in a column, I used [0,0], [0,1], [1,0] , etc instead of 0, 1, 2, etc. 

4) Now all the data was cleaned and ready to be fed through the Network in order to train it. 

## Training the Network
After training the data, it was time to train the Neural Network. The Training.py file creates a new Neural Network and feeds the newly cleaned training data through it. I then used Python's pickle process, as seen in PickledNetwork.py, in order to save an instance of the trained Network so that it did not have to be trained every time the final code was run. 

As seen in the Training.py file, the Network is created with 18 input neurons, 1 output neuron and 1 hidden layer of 15 neurons. Due to the nature of the problem the number of input and output neurons were not subject to change. But changing the number of hidden layers and neurons in each layer of a Neural Network will change its effectiveness. After testing different Network structures, the version that proved to be most effective was one with only 1 hidden layer holding 15 neurons. Any more layers or neurons and the program would have run unnecessarily long. Any fewer and it would be less accurate. 

In order to test its effectiveness I fed each applicant through the trained network and compared the Networks answer to what it is supposed to be. A number close to 1 means they would receive a loan and a number close to 0 means they would not. 

Here is a link to the outputs of the Network: https://docs.google.com/document/d/13br9rXtId7BwNRDQL9J0BWboZSKL25iR3iwKAsWEI14/edit?usp=sharing

## Conclusion
The final product of this project is written in LoanGUI.py. I created a GUI where the user can input their own information which then will be fed through the trained network and the program will return if they are eligible for a loan or not. 

Although the project works extremely well for the data provided, if the user inputs numbers that are far out of the range of the range of inputs in the data provided, then the network can have some difficulty predicting logically. In order to create an Intelligent Loan Machine that could be used on a much wider pool of applicants, I would need a much larger data set to train the Network with. Because personal banking information is so limited on the internet, this was the largest one I could find. 


## Example User Input Screen

<img width="665" alt="Screen Shot 2023-08-09 at 1 40 59 PM" src="https://github.com/jacksonbrewer3/IntelligentLoanMachine/assets/126095064/b6baf02b-b8a6-4cbf-ab5a-0f5375054efd">

## Example Success Output Screen

<img width="594" alt="Screen Shot 2023-08-09 at 1 31 44 PM" src="https://github.com/jacksonbrewer3/IntelligentLoanMachine/assets/126095064/a2aa97ef-960a-4413-ab80-bc42032ab1bd">

## Example Denial Screen

<img width="556" alt="Screen Shot 2023-08-09 at 1 48 16 PM" src="https://github.com/jacksonbrewer3/IntelligentLoanMachine/assets/126095064/9fc74d0b-37a8-4c7c-8efa-736303fe016d">
