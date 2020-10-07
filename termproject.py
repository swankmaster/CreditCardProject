# -*- coding: utf-8 -*-
"""TermProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tSeUhfspaQ5fPT8WRn2qYWylJ0yLUknD
"""

# Commented out IPython magic to ensure Python compatibility.
# Pandas is used for data manipulation
import pandas as pd
import numpy as np
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive

drive.mount('/content/drive')
data_path = '/content/drive/My Drive/Final_Project_Perceptrons'

# Read in data and display first 5 rows
creditcard = pd.read_csv(data_path + '/creditcard.csv')
creditcard.head()

# You may have to adjust the data path as needed
synthetic = pd.read_csv(data_path + '/syn_creditcard.csv')
synthetic.head()

# check for empty values
before = len(creditcard)
creditcard = creditcard.dropna()
after = len(creditcard)
print("Before NA Drpped: " + str(before))
print("After NA Drpped: " + str(after))

"""Histograms are ineffective visualizations because the data is highly imbalanced"""

creditcard.hist(column = "Class", color='b' , alpha=0.5, bins=10, figsize= (10,7))

synthetic.hist(column = "isFraud", color='b' , alpha=0.5, bins=10, figsize= (10,7))

creditcard.hist(color='b', alpha=0.5, bins=10, figsize= (25,15))

#basic eda for credit card

plt.figure(figsize = (16,12))
ax6 = sns.heatmap(creditcard.corr(),linewidths=.2)
plt.title("Heatmap of Variables")
plt.show()

creditcard.info()

# check for empty values
before1 = len(synthetic)
synthetic = synthetic.dropna()
after1 = len(synthetic)
print("Before NA Drpped: " + str(before1))
print("After NA Drpped: " + str(after1))

# converting "type" object to dummy variables

types = synthetic["type"].str.get_dummies()
#types

# joining types dataframe to the original synthetic dataframe
# and taking the original "type" column out

synthetic2 = pd.concat([synthetic, types], axis=1).drop("type", axis=1)
#synthetic2

# rearranging column order

cols_to_move = ["CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER"]
synthetic2 = synthetic2[cols_to_move + [col for col in synthetic2.columns if col not in cols_to_move]]

# eliminating string columns for model fitting

syn_no_id = synthetic2.drop(["nameOrig","nameDest"], axis=1)
syn_no_id

syn_no_id.hist(color='k', alpha=0.5, bins=10, figsize= (15,10))

#basic eda for synthetic credit card data

plt.figure(figsize = (16,12))
ax6 = sns.heatmap(syn_no_id.corr(),linewidths=.2)
plt.title("Heatmap of Variables")
plt.show()

syn_no_id.info()

creditcard_xy = creditcard
creditcard_y = creditcard['Class']
creditcard = creditcard.drop('Class', axis=1)

creditcard_y.value_counts()
not_fraud = creditcard_y.value_counts()[0]
fraud = creditcard_y.value_counts()[1]
total = fraud + not_fraud
print("The number of fraud cases is " + str(fraud) + " therefore the probability is " + str(fraud) + "/" + str(total) + " = " + str(fraud/total))
print("The number of non-fraud cases is " + str(not_fraud) + " therefore the probability is " + str(not_fraud) + "/" + str(total)+ " = " + str(not_fraud/total))

"""NULL MODEL FOR CREDITCARD.CSV

The Null model therefore assumes every case is "0" or is not fraud as this scenario is more likely. There is a higher frequency of not fraud cases in the data. Because the data is heavily skewed towards most transactions not being fraud, the null model is extremely accurate. However, we are interested in a more advanced technique so that we are able to predict when those few fraud cases would occur.
"""

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt

#Split arrays or matrices into random train and test subsets
X_train, X_test, y_train, y_test = train_test_split(creditcard, creditcard_y, test_size=0.33, random_state=4)

# create yp vector of 0s
null_yp = np.zeros(len(creditcard_y))
null_preds = np.zeros(len(y_test))

cnf_matrix = metrics.confusion_matrix(y_test, null_preds)
sns.heatmap(cnf_matrix.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test, null_preds)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test, null_preds, zero_division=1)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test, null_preds, zero_division=1)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test, null_preds, zero_division=1)))

print("Because of imbalanced class distribution, F1 score is a better metric than accuracy to evaluate the model on")

synthetic_y = syn_no_id['isFraud']
synthetic = syn_no_id.drop('isFraud', axis=1)

synthetic_y.value_counts()
not_fraud2 = synthetic_y.value_counts()[0]
fraud2 = synthetic_y.value_counts()[1]
total2 = fraud2 + not_fraud2
print("The number of fraud cases is " + str(fraud2) + " therefore the probability is " + str(fraud2) + "/" + str(total2) + " = " + str(fraud2/total2))
print("The number of non-fraud cases is " + str(not_fraud2) + " therefore the probability is " + str(not_fraud2) + "/" + str(total2)+ " = " + str(not_fraud2/total2))

#synthetic dataset

#Split arrays or matrices into random train and test subsets
X_train2, X_test2, y_train2, y_test2 = train_test_split(synthetic, synthetic_y, test_size=0.33, random_state=13)

# create yp vector of 0s
null_yp = np.zeros(len(synthetic_y))
null_preds2 = np.zeros(len(y_test2))

cnf_matrix2 = metrics.confusion_matrix(y_test2, null_preds2)
sns.heatmap(cnf_matrix2.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test2, null_preds2)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test2, null_preds2, zero_division=1)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test2, null_preds2, zero_division=1)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test2, null_preds2, zero_division=1)))

print("Because of imbalanced class distribution, F1 score is a better metric than accuracy to evaluate the model on")

"""Logistic Regression was used to predict whether a transaction was fraud."""

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
lrmodel = logreg.fit(X_train,y_train)
#predict
y_pred = logreg.predict(X_test)

from sklearn.metrics import accuracy_score

# Evaluate accuracy
print("accuracy score: " + str(accuracy_score(y_test, y_pred)))

#get confusion matrix for logreg
cnf_matrix = metrics.confusion_matrix(y_test, y_pred).T
cnf_matrix

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test, y_pred)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test, y_pred)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test, y_pred)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test, y_pred)))

print("Because of imbalanced class distribution, F1 score is a better metric than accuracy to evaluate the model on")

from sklearn.metrics import roc_auc_score, roc_curve


train_lr_predictions = lrmodel.predict(X_train)
train_lr_probs = lrmodel.predict_proba(X_train)[:, 1]

lr_probs = lrmodel.predict_proba(X_test)[:, 1]

# Calculate roc auc
lr_roc_value = roc_auc_score(y_test, lr_probs)
lr_roc_value

# coefficients and intercept

columnlist = creditcard.columns.tolist()
coef_dict = {}
for coef, feature in zip(lrmodel.coef_[0,:], columnlist):
  coef_dict[feature] = coef

print(coef_dict)
print("intercept: " + str(lrmodel.intercept_))

# feature importance

from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectFromModel

smf = SelectFromModel(lrmodel, threshold=-np.inf, max_features=8)
smf.fit(X_train, y_train)
feature_idx = smf.get_support()
feature_name = X_train.columns[feature_idx]
feature_name

#tried getting feature importances, but only could get coefficients

smf.transform(X_train)

feature_name_t = tuple(X_train.columns[feature_idx])
important_coef = {}
for i in feature_name_t:
  important_coef[i] = coef_dict.get(i)
print(important_coef)

plt.bar(important_coef.keys(), important_coef.values())
plt.ylabel("coefficients")
plt.xlabel("important features")
plt.title("feature importance")

#scaling amount column
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()

def scaleColumns(df, cols_to_scale):
    for col in cols_to_scale:
        df[col] = pd.DataFrame(min_max_scaler.fit_transform(pd.DataFrame(df[col])),columns=[col])
    return df

scaled_credit = scaleColumns(creditcard, ["Amount"])
scaled_credit

# we tried scaling the amount column on the credit card dataset

#Split arrays or matrices into random train and test subsets
s_X_train, s_X_test, y_train, y_test = train_test_split(scaled_credit, creditcard_y, test_size=0.33, random_state=4)

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
lrmodel_ = logreg.fit(s_X_train,y_train)
#predict
y_pred_ = logreg.predict(s_X_test)

# Evaluate accuracy
print("accuracy score: " + str(accuracy_score(y_test, y_pred_)))

#get confusion matrix for logreg
cnf_matrix_ = metrics.confusion_matrix(y_test, y_pred_).T
cnf_matrix_

from sklearn.metrics import roc_auc_score, roc_curve


train_lr__predictions = lrmodel_.predict(s_X_train)
train_lr__probs = lrmodel_.predict_proba(s_X_train)[:, 1]

lr_probs_ = lrmodel_.predict_proba(s_X_test)[:, 1]

# Calculate roc auc
lr_roc_value_ = roc_auc_score(y_test, lr_probs_)
lr_roc_value_

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test, y_pred_)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test, y_pred_)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test, y_pred_)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test, y_pred_)))

# coefficients and intercept

columnlist = creditcard.columns.tolist()
coef_dict_ = {}
for coef, feature in zip(lrmodel_.coef_[0,:], columnlist):
  coef_dict_[feature] = coef

print(coef_dict_)
print("intercept: " + str(lrmodel_.intercept_))

# feature importance


smf_ = SelectFromModel(lrmodel_, threshold=-np.inf, max_features=8)
smf_.fit(s_X_train, y_train)
s_feature_idx = smf_.get_support()
s_feature_name = s_X_train.columns[s_feature_idx]
s_feature_name

smf_.transform(s_X_train)

s_feature_name_t = tuple(s_X_train.columns[s_feature_idx])
s_important_coef = {}
for i in s_feature_name_t:
  s_important_coef[i] = coef_dict_.get(i)
print(important_coef)

plt.bar(s_important_coef.keys(), s_important_coef.values())
plt.ylabel("coefficients")
plt.xlabel("important features")
plt.title("feature importance")

# fit the model with data
lrmodel2 = logreg.fit(X_train2,y_train2)
#predict
y_pred2 = logreg.predict(X_test2)

# Evaluate accuracy
print("accuracy score: " + str(accuracy_score(y_test2, y_pred2)))

#get confusion matrix for logreg
cnf_matrix2 = metrics.confusion_matrix(y_test2, y_pred2).T
cnf_matrix2

train_lr2_predictions = lrmodel2.predict(X_train2)
train_lr2_probs = lrmodel2.predict_proba(X_train2)[:, 1]

lr_probs2 = lrmodel2.predict_proba(X_test2)[:, 1]

# Calculate roc auc
lr_roc_value2 = roc_auc_score(y_test2, lr_probs2)
lr_roc_value2

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test2, y_pred2)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test2, y_pred2)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test2, y_pred2)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test2, y_pred2)))

print("Because of imbalanced class distribution, F1 score is a better metric than accuracy to evaluate the model on")
print("\n")
print("Credit card data has better F1 score (0.7368) compared to synthetic data (0.4384)")

# coefficients and intercept

columnlist2 = synthetic.columns.tolist()
coef_dict2 = {}
for coef, feature in zip(lrmodel2.coef_[0,:], columnlist2):
  coef_dict2[feature] = coef

print(coef_dict2)
print("intercept: " + str(lrmodel2.intercept_))

# feature importance


smf2 = SelectFromModel(lrmodel2, threshold=-np.inf, max_features=8)
smf2.fit(X_train2, y_train2)
feature_idx2 = smf2.get_support()
feature_name2 = X_train2.columns[feature_idx2]
feature_name2

smf2.transform(X_train2)

feature_name_t2 = tuple(X_train2.columns[feature_idx2])
important_coef2 = {}
for i in feature_name_t2:
  important_coef2[i] = coef_dict2.get(i)
print(important_coef2)

plt.bar(important_coef2.keys(), important_coef2.values())
plt.ylabel("coefficients")
plt.xlabel("important features")
plt.title("feature importance")

# scaling certain columns from synthetic data

scaled_synthetic = scaleColumns(synthetic, ["step", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"])
scaled_synthetic

# with the scaled synthetic data

#Split arrays or matrices into random train and test subsets
s_X_train2, s_X_test2, y_train2, y_test2 = train_test_split(scaled_synthetic, synthetic_y, test_size=0.33, random_state=4)

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
lrmodel2_ = logreg.fit(s_X_train2,y_train2)
#predict
y_pred2_ = logreg.predict(s_X_test2)

# Evaluate accuracy
print("accuracy score: " + str(accuracy_score(y_test2, y_pred2_)))

#get confusion matrix for logreg
cnf_matrix2_ = metrics.confusion_matrix(y_test2, y_pred2_).T
cnf_matrix2_

train_lr2__predictions = lrmodel2_.predict(s_X_train2)
train_lr2__probs = lrmodel2_.predict_proba(s_X_train2)[:, 1]

lr_probs2_ = lrmodel2_.predict_proba(s_X_test2)[:, 1]

# Calculate roc auc
lr_roc_value2_ = roc_auc_score(y_test2, lr_probs2_)
lr_roc_value2_

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test2, y_pred2_)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test2, y_pred2_)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test2, y_pred2_)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test2, y_pred2_)))

# coefficients and intercept

columnlist2_ = synthetic.columns.tolist()
coef_dict2_ = {}
for coef, feature in zip(lrmodel2_.coef_[0,:], columnlist2_):
  coef_dict2_[feature] = coef

print(coef_dict2_)
print("intercept: " + str(lrmodel2_.intercept_))

# feature importance


smf2_ = SelectFromModel(lrmodel2_, threshold=-np.inf, max_features=8)
smf2_.fit(s_X_train2, y_train2)
feature_idx2_ = smf2_.get_support()
feature_name2_ = s_X_train2.columns[feature_idx2_]
feature_name2_

smf2_.transform(s_X_train2)

feature_name_t2_ = tuple(s_X_train2.columns[feature_idx2_])
important_coef2_ = {}
for i in feature_name_t2_:
  important_coef2_[i] = coef_dict2_.get(i)
print(important_coef2_)

plt.bar(important_coef2_.keys(), important_coef2_.values())
plt.ylabel("coefficients")
plt.xlabel("important features")
plt.title("feature importance")

"""Below are the NaiveBayesels for the creditcard.csv data.

First, we use a gaussian model.
"""

from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

features = ["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"]
# Initialize our classifier
gnb = GaussianNB()

# Train our classifier
model_nb = gnb.fit(X_train, y_train)
preds = gnb.predict(X_test)
print(preds)

from sklearn import datasets, naive_bayes, metrics, feature_extraction
from sklearn.metrics import accuracy_score

# Evaluate accuracy
print(accuracy_score(y_test, preds))

from sklearn.metrics import confusion_matrix

mat = confusion_matrix(y_test, preds)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test, preds)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test, preds)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test, preds)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test, preds)))

print("Because of imbalanced class distribution, F1 score is a better metric than accuracy to evaluate the model on")

"""Below are the NaiveBayesels for the Synthetic data"""

synthetic_y = syn_no_id['isFraud']
synthetic = syn_no_id.drop('isFraud', axis=1)

#Split arrays or matrices into random train and test subsets
X_train2, X_test2, y_train2, y_test2 = train_test_split(synthetic, synthetic_y, test_size=0.33, random_state=13)

# Initialize our classifier
gnb = GaussianNB()

# Train our classifier
model_nb2 = gnb.fit(X_train2, y_train2)
preds2 = gnb.predict(X_test2)
print(preds2)

# Evaluate accuracy
print(accuracy_score(y_test2, preds2))

#confusion matrix
mat = confusion_matrix(y_test2, preds2)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
print(metrics.classification_report(y_test2, preds2, zero_division=1))

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test2, preds2)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test2, preds2)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test2, preds2)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test2, preds2)))

"""Below is code attempting to do RandomForest Classification on creditcard data"""

from sklearn.ensemble import RandomForestClassifier

# Create the model with 100 trees
model_rf = RandomForestClassifier(max_features=27, max_depth=2 ,n_estimators=10, random_state=3, criterion='entropy', n_jobs=1, verbose=1 )# Fit on training data
model_rf.fit(X_train, y_train)

# Actual class predictions
rf_predictions = model_rf.predict(X_test)
# Probabilities for each class
rf_probs = model_rf.predict_proba(X_test)[:, 1]

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

#params of the model
param_grid = {"max_depth": [3,5, None],
              "n_estimators":[5,10],
              "max_features": [5,10,15]}

grid_search = GridSearchCV(model_rf, param_grid=param_grid, cv=5, scoring='recall')
grid_search.fit(X_train, y_train)

print(grid_search.best_score_)
print(grid_search.best_params_)

rf = RandomForestClassifier(max_depth=None, max_features = 15, n_estimators = 10)
rf.fit(X_train, y_train)
print(rf.feature_importances_)

features = ["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"]

plt.figure(figsize = (9,5))

feat_import = pd.DataFrame({'Feature': features, 'Feature importance': rf.feature_importances_})
feat_import = feat_import.sort_values(by='Feature importance',ascending=False)

g = sns.barplot(x='Feature',y='Feature importance',data=feat_import)
g.set_xticklabels(g.get_xticklabels(),rotation=90)
g.set_title('Features importance - Random Forest',fontsize=20)
plt.show()

# Evaluate accuracy
print(accuracy_score(y_test, rf_predictions))

#confusion matrix
matrf = confusion_matrix(y_test, rf_predictions)
sns.heatmap(matrf.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')

#accuracy
print("The accuracy score is " + str(metrics.accuracy_score(y_test, rf_predictions)))

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test, rf_predictions)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test, rf_predictions)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test, rf_predictions)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test, rf_predictions)))

#y_pred_proba = clf.predict_proba(X_test)[::,1]
#fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
#auc = metrics.roc_auc_score(y_test, y_pred_proba)
#plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
#plt.legend(loc=4)
#plt.show()

from sklearn.metrics import precision_score, recall_score, roc_auc_score, roc_curve


train_rf_predictions = model_rf.predict(X_train)
train_rf_probs = model_rf.predict_proba(X_train)[:, 1]

# Calculate roc auc
roc_value = roc_auc_score(y_test, rf_probs)
roc_value

"""Below is the code for a RandomForestClassifier model for the synthetic data."""

# Create the model with 100 trees
model_rf2 = RandomForestClassifier(max_features=8, max_depth=2 ,n_estimators=10, random_state=3, criterion='entropy', n_jobs=1, verbose=1 )

#params of the model
param_grid = {"max_depth": [3,5, None],
              "n_estimators":[3,5,7],
              "max_features": [4,5,7]}

grid_search2 = GridSearchCV(model_rf2, param_grid=param_grid, cv=5, scoring='recall')
grid_search2.fit(X_train2, y_train2)

print(grid_search2.best_score_)
print(grid_search2.best_params_)

rf2 = RandomForestClassifier(max_depth=5, max_features = 4, n_estimators = 7)
rf2.fit(X_train2, y_train2)
print(rf2.feature_importances_)

features2 = ["CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER","step","amount","olbalanceOrg","newbalanceOrig","oldbalanceDest","newbalanceDest","isFlaggedFraud"]

plt.figure(figsize = (9,5))

feat_import2 = pd.DataFrame({'Feature': features2, 'Feature importance': rf2.feature_importances_})
feat_import2 = feat_import2.sort_values(by='Feature importance',ascending=False)

g2 = sns.barplot(x='Feature',y='Feature importance',data=feat_import2)
g2.set_xticklabels(g2.get_xticklabels(),rotation=90)
g2.set_title('Features importance - Random Forest',fontsize=20)
plt.show()

"""Below is an IsolationForest prediction for the creditcard data."""

from sklearn.ensemble import IsolationForest

clf = IsolationForest(behaviour='new', max_samples=len(X_train), random_state=2, contamination='auto')
clf.fit(X_train)
y_pred_clf = clf.predict(X_test)

# Reshape the prediction values to 0 for valid, 1 for fraud. 
y_pred_clf[y_pred_clf == 1] = 0
y_pred_clf[y_pred_clf == -1] = 1
#print confusion matrix
clf_matrix = confusion_matrix(y_test, y_pred_clf)
clf_matrix

#accuracy
print("The accuracy score is " + str(metrics.accuracy_score(y_test, y_pred_clf)))

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test, y_pred_clf)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test, y_pred_clf)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test, y_pred_clf)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test, y_pred_clf)))

"""Below is an IsolationForest model for the synthetic dataset."""

clf2 = IsolationForest(behaviour='new', max_samples=len(X_train), random_state=2, contamination='auto')
clf2.fit(X_train2)
y_pred_clf2 = clf2.predict(X_test2)

# Reshape the prediction values to 0 for valid, 1 for fraud. 
y_pred_clf2[y_pred_clf2 == 1] = 0
y_pred_clf2[y_pred_clf2 == -1] = 1
#print confusion matrix
clf_matrix2 = confusion_matrix(y_test2, y_pred_clf2)
clf_matrix2

#accuracy
print("The accuracy score is " + str(metrics.accuracy_score(y_test2, y_pred_clf2)))

#error rate
print("The error rate is " + str(1 - metrics.accuracy_score(y_test2, y_pred_clf2)))

#precision
print("The precision score is " + str(metrics.precision_score(y_test2, y_pred_clf2)))

#recall
print("The recall score is " + str(metrics.recall_score(y_test2, y_pred_clf2)))

#F1 score
print("The F1 score is " + str(metrics.f1_score(y_test2, y_pred_clf2)))

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasRegressor
from keras.layers import Dense
from keras import optimizers
import sys
ccPath = '/content/drive/My Drive/creditcard.csv'
synPath = '/content/drive/My Drive/syn_creditcard.csv'
neelCC = pd.read_csv(ccPath)
neel_syn = pd.read_csv(synPath)

def getMetrics(model,x_te,y_te,ratio):
  preds_m = model.predict(x_te)
  pred = []
  for nF,f in preds_m:
    if (nF / f) > ratio:
      pred.append('noFraud')
    else:
      pred.append('Fraud')
  t = []
  for nF,f in y_te.to_numpy():
    if nF > f:
      t.append('noFraud')
    else:
      t.append('Fraud')
  preds = pd.DataFrame(t,columns=['True'])
  preds['Model Predictions'] = pred
  preds['count'] = y_te[y_te.columns[0]]
  h = preds.groupby(['True','Model Predictions']).count().unstack()
  TP = h[h.columns[0]]['Fraud']
  FN = h[h.columns[0]]['noFraud']
  FP = h[h.columns[1]]['Fraud']
  TN = h[h.columns[1]]['noFraud']
  recall = TP/(TP+FN)
  precision = TP/(TP+FP)
  f_m = (2*recall*precision)/(recall+precision)
  conf = h
  return recall,precision,f_m,conf

def scaleX(x,xcols,activation_f):
  activation_types = {
      'sigmoid': [0,1,'exclusive'],
      'tanh': [-1,1,'exclusive'],
      'reLu': [0,None,'inclusive'],
      'le_reLu': [None,None,'inclusive']
  }
  ub = activation_types[activation_f][1]
  lb = activation_types[activation_f][0]
  tranX = pd.DataFrame(columns=xcols)
  for i in range(len(xcols)):
    x_i = x.to_numpy()[:,i]
    max_x = max(x_i)
    min_x = min(x_i)
    scale = (ub-lb)/(max_x - min_x)
    x_tran = (x_i - min_x)*scale + lb
    tranX[xcols[i]] = x_tran
  return tranX

def scaleY(y,activation_f):
  activation_types = {
      'sigmoid': [0,1,'exclusive'],
      'tanh': [-1,1,'exclusive'],
      'reLu': [0,None,'inclusive'],
      'le_reLu': [None,None,'inclusive']
  }
  ub = activation_types[activation_f][1]
  lb = activation_types[activation_f][0]
  y_i = y
  maxY = max(y_i)
  minY = min(y_i)
  scale = (ub-lb)/(maxY-minY)
  y_tran = (y_i-minY)*scale + lb
  return y_tran

def unscaleY(minY,maxY,y_s,activation_f):
  activation_types = {
      'sigmoid': [0,1,'exclusive'],
      'tanh': [-1,1,'exclusive'],
      'reLu': [0,None,'inclusive'],
      'le_reLu': [None,None,'inclusive']
  }
  ub = activation_types[activation_f][1]
  lb = activation_types[activation_f][0]
  y_i = y_s
  scale = (ub-lb)/(maxY-minY)
  unscaled = (y_i-lb)/scale +minY
  return unscale


def buildSimpleModel(sizes,input_lay):
  nx = input_lay
  model = base_model = tf.keras.Sequential([
          tf.keras.layers.Dense(sizes[1],input_shape=(nx,),activation = 'sigmoid',
                                weights = [np.zeros([nx,sizes[1]]),np.zeros([sizes[1]])]),
          tf.keras.layers.Dense(sizes[2], activation = 'tanh'),
          tf.keras.layers.Dense(sizes[3], activation = 'sigmoid')]
      )
  return model
  
def cross_validation(model,optime,x,y,batch,epochs):
  model = model
  opt = optime
  x = x
  y = y
  # xcols = xcols
  r = []
  # ep = int(input("Epochs:"))
  # batch = int(input("batchSize:"))
  sz = int(x.shape[0]/10)
  p = np.random.permutation(x.shape[0])
  model.compile(loss ='binary_crossentropy',optimizer = optime,metrics= ['acc'])
  for i in range(10):
    lb = i*sz
    ub = (i+1)*sz
    test = p[lb:ub]
    train = np.concatenate((p[:lb],p[ub:]),axis = None)
    
    model.fit(x[train],y[train],batch_size=batch,epochs = epochs,verbose = 0)
    r.append(model.evaluate(x[test],y[test])[1])
  accCV = sum(r)/10
  # estimator = KerasRegressor(build_fn=baseline(model,optime,xcols),epochs = ep,batch_size = batch,verbose = 0)
  # estimator.fit(x,y)
  # rCV = cross_val_score(estimator,x,y,scoring = 'r2',cv = 10)
  return accCV

def compile_fit_evaluate(model,opt,activation_type,cols_x,x,y,batch,epochs):
  # x = data[xcols]
  # print(activation_type)
  x = scaleX(x,cols_x,activation_type)
  batch = batch
  epochs = epochs
  # rCV = cross_validation(model,opt,x,y,batch,epochs)
  model.compile(loss = 'binary_crossentropy',optimizer = opt,metrics=['acc'])
  model.fit(x,y,batch_size = batch,epochs = epochs, verbose = 0)
  r2 = model.evaluate(x,y)[-1]
  n = len(x)
  p = len(x.T)
  side = (n-1)/(n-p-1)
  adjR2 = 1-((1-r2)*side)
  row = [r2,adjR2]
  return row

def test_compile(model,opt,activation_type,x,y,batch,epochs,xcols):
  x = scaleX(x,xcols,activation[0])
  model.compile(loss ='binary_crossentropy',optimizer = opt,metrics = ['acc'])
  model.fit(x,y,batch_size = batch,epochs = epochs,verbose = 0)
  r2 = model.evaluate(x,y)[0]
  return r2

def forwardSel (cols, data,xcolumns,y,index_q,model,opt,activation,batch,epochs):
  rg_j = model
  batch = batch
  epochs = epochs
  j_mx = -1 # best column, so far
  fit_mx = - sys.float_info.max # best fit, so far
  print ("start for loop")
  sz = len(cols)
  unordered = []
  for j in xcolumns:
    print ("process column ", j)
    cols_j = cols.copy()
    if not j in cols:
      cols_j.append(j) # try adding variable x_j
      # x_cols = [ data[index] for index in cols_j ] # x projected onto cols_j
      # (rg_j,layers,opt,minY,maxY,x,y) = buildModel(data,cols_j,index_y,layers) # regress with x_j added
      x = data[cols_j]
      r2 = compile_fit_evaluate(rg_j,opt,activation[0],cols_j,x,y,batch,epochs)
      unordered.append(r2[index_q])
      fit_j = r2[index_q] # new fit for first response
      if fit_j > fit_mx:
        j_mx = [j]
        fit_mx = fit_j
        r_mx = r2.copy()
    # elif len(cols) == len(xcolumns):
    #   r2 = compile_fit_evaluate(rg_j,opt,activation,cols_j,x,y,batch,epochs)
    #   fit_j = r2[index_q]
    #   return j_mx,rg_j,r2
  if sz == 0:
    df = pd.DataFrame(data=unordered,columns = ['Acc'])
    df['cols'] = xcolumns
    if len (xcolumns) > 25:
      df = df[df.Acc > 0.99835].sort_values(by = ['Acc'], ascending = False)
    else:
      df = df[df.Acc > 0.99895].sort_values(by = ['Acc'], ascending = False)
    j_mx = list(df.cols)
    return j_mx,rg_j,r_mx
    

  if j_mx == -1:
    print ("forwardSel: could not find a variable x_j to add: j = -1")
  return j_mx, rg_j,r_mx # return best column

def forwardSelAll (index_q,batch, epochs, params, data,sizes,xcolumns,y,activation):
    r2 = pd.DataFrame(columns = ['acc','acc_Adj'])
    # batch = int(input("Batch size"))
    # epochs = int(input("Epochs:"))
    activation =['sigmoid','tanh','sigmoid']
    cols = []
    models = []
    dim = len(data)
    # layers = int(input("Number of layers(more than 2 less than 4)"))
    # (model,layers,opt,minY,maxY,xcols,y,activation,hidden) = buildModel(data,1,xcolumns,y,layers)
    opt = tf.keras.optimizers.Adam(params[0],params[1],params[2])
    base_model = tf.keras.Sequential([
          tf.keras.layers.Dense(sizes[1],input_shape=(1,),activation = 'sigmoid',
                                weights = [np.zeros([1,sizes[1]]),np.zeros([sizes[1]])]),
          tf.keras.layers.Dense(sizes[2], activation = 'tanh'),
          tf.keras.layers.Dense(sizes[3], activation = 'sigmoid')]
      )
    # base_model.compile(loss = 'binary_crossentropy', optimizer = opt, metrics = ['mae','acc'])
    shape = len(y.shape)
    index = 0
    # print(activation)
    for i in range(dim):
      print('Iteration' + str(i))
      if len(xcolumns) == len(cols):
        break
      (j, model_j,rSq) = forwardSel(cols, data,xcolumns,y,1,base_model,opt,activation,batch,epochs)
      models.append(model_j)
      if len(cols) == 0:
        cols = j
      else:
        
        cols.append(j[0])
      # cols.append(j)
      r2.loc[index] = rSq
      index = index + 1
      input_l = len(cols) + 1
      # add an if statement to get the figure out when rSq is at an apex and save model
      if rSq[1] > max(r2.acc_Adj):
        bestCols = cols.copy()
        bestModel = model_j
        return bestCols,bestModel,r2
      base_model=buildSimpleModel(sizes,input_l)
    # rSq = model_j.getRsq()
    return cols,models,r2

from sklearn.model_selection import train_test_split
xcols = neelCC.columns[:-1]
x = neelCC[xcols]
y = pd.get_dummies(neelCC['Class'])
x_trCC,x_teCC,y_trCC,y_teCC = train_test_split(x,y,test_size = 0.33, random_state = 4)
x_trCC = scaleX(x_trCC,xcols,'sigmoid')
x_teCC = scaleX(x_teCC,xcols,'sigmoid')
cc_size = [len(xcols),16,4,2]
opt = tf.keras.optimizers.Adam(0.07,0.93,0.99)
params = [0.07,0.93,0.99]
activation = ['sigmoid','tanh','sigmoid']
batch = 500
epochs = 15
cc = {
    'size': cc_size,
    'activation':activation,
    'batch':batch,
    'epochs':epochs,
    'xcols':xcols
}
(columns_in,all_nets,r2) = forwardSelAll(0,cc['batch'],cc['epochs'],params,x_trCC,cc['size'],cc['xcols'],y_trCC,cc['activation'])

ind = r2['acc'].idxmax()
cc_Best = all_nets[idx]
cc_Best.compile(loss = 'binary_crossentropy', optimizer = opt, metrics = ['mae','acc'])
cc_Best.fit(x_trCC[columns_in[:13]],y_trCC, batch_size = 500, epochs = 30)
print(cc_Best.evaluate(x_teCC[columns_in[:13]],y_teCC)[-1])
(recallcc,precisioncc,f_cc,confusionCC) = getMetrics(cc_Best,x_teCC[columns_in[:13]],y_teCC,1)
print("Recall: " + str(recallcc))
print("Precision: " + str(precisioncc))
print("F1 Score: " + str(f_cc))
print("Confusion Matrix: ")
print("")
print(confusionCC)
# all_nets[5].fit(x_teCC[columns_in[:13]],y_teCC)

x = neel_syn[neel_syn.columns[:-2]]
dummies = pd.get_dummies(x.type)
x = pd.concat([x,dummies],axis = 1).drop('type',axis = 1)
x = x.drop(['nameOrig','nameDest'],axis = 1)
y = pd.get_dummies(neel_syn['isFraud'])
y = y.rename(columns={0:'notFraud',1:'isFraud'})

xcols = list(x.columns)
x_tr,x_te,y_trSyn,y_teSyn=train_test_split(x,y,test_size = 0.33, random_state = 4)
x_trSyn = scaleX(x_tr,x_tr.columns,'sigmoid')
x_teSyn = scaleX(x_te,x_te.columns,'sigmoid')
params = [0.01,0.93,0.99]
activation = ['sigmoid','tanh','sigmoid']
syn_size = [len(xcols),8,4,2]
batch = 5000
epochs = 15
syn = {
    'size': cc_size,
    'activation':activation,
    'batch':batch,
    'epochs':epochs,
    'xcols':xcols
}
(columns_in,syn_nets,syn_r2) = forwardSelAll(0,syn['batch'],syn['epochs'],params,x_trSyn,syn['size'],syn['xcols'],y_trSyn,syn['activation'])

ind = syn_r2['acc'].idxmax()
syn_Best = syn_nets[ind]
syn_Best.compile(loss = 'binary_crossentropy', optimizer = opt, metrics = ['mae','acc'])
syn_Best.fit(x_trSyn[columns_in[:ind+1]],y_trSyn, batch_size = 500, epochs = 10)
print(syn_Best.evaluate(x_teSyn[columns_in[:ind+1]],y_teSyn)[-1])
(recallsyn,precisionsyn,f_syn,confusionSyn) = getMetrics(syn_Best,x_teSyn[columns_in[:ind+1]],y_teSyn,4)
print("Recall: " + str(recallsyn))
print("Precision: " + str(precisionsyn))
print("F1 Score: " + str(f_syn))
print("Confusion Matrix: ")
print("")
print(confusionSyn)

ind