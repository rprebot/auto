import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd
from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn.svm import SVC

def pca(data, components):
	""" Plot variances explaines by PC"""

	_pca = PCA(n_components = components)
	_pca.fit(data)
	var = _pca.explained_variance_ratio_
	cum_var = np.cumsum(np.round(var, decimals=4)*100)
	fig = plt.plot(cum_var)
	rotation = pd.DataFrame(
		_pca.components_,
		columns = data.columns,
		index = ['PC-1','PC-2','PC-3','PC-4','PC-5','PC-6','PC-7','PC-8','PC-9',]
		)

	return (fig, rotation)


def cross_val_logistic_regression(variables, targeted):
	""" Classification report for the Pipeline PCA + Logistic"""

	logistic = linear_model.LogisticRegression()
	pca = decomposition.PCA()
	pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])

	n_components = [4,5]
	Cs = np.logspace(-10,10,10)

	estimator = GridSearchCV(
		pipe,
		dict(pca__n_components = n_components,
			logistic__C = Cs)
		)
	
	predicted = cross_val_predict(
	estimator, variables, targeted, cv = 5)

	return {
		'accuracy':metrics.accuracy_score(targeted, predicted),
		'report':metrics.classification_report(targeted, predicted)
		}

def cross_val_SVM_linear(variables, targeted):
	""" Classification report for the Pipeline PCA + SVM Linear"""

	svm = SVC(kernel = "linear")
	pca = decomposition.PCA()
	pipe = Pipeline(steps=[('pca', pca), ('svm', svm)])

	n_components = [4,5]
	C = np.logspace(-10,10,10)

	estimator = GridSearchCV(
		pipe,
		dict(pca__n_components = n_components,
			svm__C = C)
		)
	
	predicted = cross_val_predict(
	estimator, variables, targeted, cv = 5)

	return {
		'accuracy':metrics.accuracy_score(targeted, predicted),
		'report':metrics.classification_report(targeted, predicted)
		}

def cross_val_SVM_RBF(variables, targeted):
	""" Classification report for the Pipeline PCA + SVM RBF"""

	svm = SVC(kernel = "rbf")
	pca = decomposition.PCA()
	pipe = Pipeline(steps=[('pca', pca), ('svm', svm)])

	n_components = [4,5]
	C = np.logspace(-10,10,10)

	estimator = GridSearchCV(
		pipe,
		dict(pca__n_components = n_components,
			svm__C = C)
		)
	
	predicted = cross_val_predict(
	estimator, variables, targeted, cv = 5)

	return {
		'accuracy':metrics.accuracy_score(targeted, predicted),
		'report':metrics.classification_report(targeted, predicted)
		}
