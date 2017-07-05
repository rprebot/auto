import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import exploratory_analysis as ea
import machine_learning as ml
import pandas as pd

auto_numeric = ea.auto_numeric()
auto_category = ea.auto_category()
risk = ea.targeted()

# Performing the PCA
fig_pca, rotation_pca = ml.pca(auto_numeric, 9)
plt.show(fig_pca)
print(rotation_pca)


# Cross Validation on a chain line PCA + Logistic Regression
log_regr = ml.cross_val_logistic_regression(
		auto_numeric, risk)

print(log_regr['report'])


# Cross Validation on a chain line PCA + SVM Linear
svm_lin = ml.cross_val_SVM_linear(
		auto_numeric, risk)

print(svm_lin['report'])


# Cross Validation on a chain line PCA + SVM RBF
svm_rbf = ml.cross_val_SVM_RBF(
		auto_numeric, risk)

print(svm_rbf['report'])


# Add categorical one by one
_variables = auto_numeric

_columns = auto_category.columns[0]

for _columns in auto_category.columns:
	_variables[_columns] = auto_category[_columns]
	_variables = pd.get_dummies(_variables)
	svm_rbf = ml.cross_val_SVM_RBF(
		_variables, risk)
	print("%s \t %f \n"
		% (_columns, svm_rbf['accuracy'])
		)



# With aspiration
auto_numeric = ea.auto_numeric()
auto_numeric['aspiration'] = auto_category['aspiration']
auto_numeric['body-style'] = auto_category['body-style']
auto_numeric['engine-location'] = auto_category['engine-location']

auto_numeric = pd.get_dummies(auto_numeric)
svm_rbf = ml.cross_val_SVM_RBF(
	auto_numeric, risk)
print(svm_rbf['report'])


