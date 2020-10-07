# CreditCardProject
Term project for my Data Science 2 class. This project was done with partner: Riley Pinion and Hannah (Heejae) Lee.

NOTES:
	•	The notebook is made up of methods which are called upon based on the model used. More in detail compilation instructions will be found later on in the doc.
	•	The datasets are imported from the Google Drive, so the pathway listed may not be the same pathway that the data is stored on your drive or local machine

NEURAL NET 4L
The datasets are loaded separately and the pathway is different than all prior models. Any method not documented is not directly accessed by the user. Output 
related to forwardSelection listed in notebook has a larger batch size and smaller number of epochs due to length of runtime

def getMetrics(model,x_te,y_te,ratio):
The getMetrics method takes in 4 positional arguments: model (whatever model the metrics should correspond to), x_te and y_te (the testing sets derived from 
train_test_split), and ratio (the ratio at which an observation is Fraud or notFraud).
return recall,precision,f_m,conf
The method returns 4 objects: recall (TP/TP + FN), precision (TP/TP + FP), f_m (the F1 statistic), and conf (the confusion matrix). Rows are actual observations, 
and columns are predicted outputs.


def scaleX(x,xcols,activation_f)
scaleX scales each X column based on the activation function of the input layer.
return tranX
returns a data frame of all the transformed x values.

def scaleY(y,activation_f):
same as above but for y columns

def buildSimpleModel(sizes,input_lay)
The buildSimpleModel method takes two parameters: sizes (a list of 4 values – input layer size, 1st hidden layer size, 2nd hidden layer size, output size) and 
input_lay (the size of the input layer at said iterations).
return model
returns a Sequential model object.



def forwardSel (cols, data,xcolumns,y,index_q,model,opt,activation,batch,epochs)
The forwardSel method takes in 10 parameters. Cols is the columns that are currently in the model, data is the x matrix, y is the vector/matrix, index_q is the 
index of the accuracy var that is needs to be evaluated, model is the model, opt is the optimizer, activation is a list of all the activation functions in the 
model, batch is the batch size, epochs is number of epochs.
return j_mx, rg_j,r_mx
Returns 3 objects, j_mx is a list of the best columns (on the first iteration it takes all variables with accuracy better than the null model for time sake), rg_j 
is the model structure (keras object), r_mx is the best row of accuracy metrics.

def forwardSelAll (index_q,batch, epochs, params, data,sizes,xcolumns,y,activation)
The forwardSelAll method takes in 9 parameters. The parameters: index_q is the index of which metric the best column is to be judged on, batch is batch size,
epochs is the number of epochs that are run, data is the x matrix, xcolumns are all x column names, y is the y vector/matrix, activation is a list of all 
activation functions in the model.
